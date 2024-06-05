import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.StandardOpenOption;

public class Instance implements Runnable {
    private final int UUID;
    private final String instrcRReadyPath;
    private final String instrcRPath;
    private final String instrcSPath;
    private final String instrcRCompletePath;

    public Instance(int UUID) {
        this.UUID = UUID;
        this.instrcRReadyPath = "Comp" + UUID + "/Instrc_r_ready.txt";
        this.instrcRPath = "Comp" + UUID + "/Instrc_r.txt";
        this.instrcSPath = "Comp" + UUID + "/Instrc_s.txt";
        this.instrcRCompletePath = "Comp" + UUID + "/Instrc_r_complete.txt";
    }

    public void processCommands() {
        try {
            while (true) {
                // Check if there's a new command to process
                String readyFlag = readStringFromFile(instrcRReadyPath);
                if (!readyFlag.trim().equals("ready")) {
                    Thread.sleep(1);
                    continue;
                }

                // Read the command from Instrc_r.txt
                String command = readStringFromFile(instrcRPath).trim();
                String[] parts = command.split(" ");
                if (parts.length < 3) {
                    // Handle invalid command format
                    System.err.println("Error: Invalid command format in Instrc_r.txt");
                    continue;
                }

                // Parse command parameters
                double A, B;
                try {
                    A = Double.parseDouble(parts[0]);
                    B = Double.parseDouble(parts[1]);
                } catch (NumberFormatException e) {
                    // Handle invalid numeric input
                    System.err.println("Error: Invalid numeric input in command file.");
                    continue;
                }
                String type = parts[2];

                // Process the command
                String resultStr = processCommand(A, B, type);

                // Write the result to Instrc_s.txt
                writeStringToFile(instrcSPath, resultStr);

                // Signal completion of command processing
                writeStringToFile(instrcRCompletePath, "complete");

                // Clear readiness for the next command
                writeStringToFile(instrcRReadyPath, "");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private String processCommand(double A, double B, String type) {
        switch (type) {
            case "A":
                return String.valueOf(A + B);
            case "S":
                return String.valueOf(A - B);
            case "M":
                return String.valueOf(A * B);
            case "D":
                if (B != 0) {
                    return String.valueOf(A / B);
                } else {
                    System.err.println("Error: Division by zero.");
                    return "";
                }
            case "IF=":
                return A == B ? "T" : "F";
            case "IF!":
                return A != B ? "T" : "F";
            case "IF>":
                return A > B ? "T" : "F";
            case "IF<":
                return A < B ? "T" : "F";
            default:
                System.err.println("Error: Unknown command type.");
                return "";
        }
    }

    private String readStringFromFile(String filePath) {
        try {
            return new String(Files.readAllBytes(Paths.get(filePath))).trim();
        } catch (Exception e) {
            e.printStackTrace();
            return "";
        }
    }

    private void writeStringToFile(String filePath, String content) {
        try {
            Files.write(Paths.get(filePath), content.getBytes(), StandardOpenOption.CREATE,
                    StandardOpenOption.TRUNCATE_EXISTING);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    @Override
    public void run() {
        processCommands();
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java Instance <UUID>");
            System.exit(1);
        }

        int UUID = Integer.parseInt(args[0]);
        Instance instance = new Instance(UUID);
        instance.run();
    }
}
