import java.io.*;
import java.net.ServerSocket;
import java.net.Socket;

public class Instance implements Runnable {
    private final int port;

    public Instance(int port) {
        this.port = port;
    }

    @Override
    public void run() {
        try (ServerSocket serverSocket = new ServerSocket(port)) {
            System.out.println("Instance " + port + " listening on port " + port);

            while (true) {
                try (Socket clientSocket = serverSocket.accept();
                     BufferedReader in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
                     PrintWriter out = new PrintWriter(clientSocket.getOutputStream(), true)) {

                    //System.out.println("Instance " + port + ": Client connected");

                    String command = in.readLine();
                    //System.out.println("Instance " + port + ": Received command '" + command + "'");
                    if (command != null) {
                        String[] parts = command.split(" ");
                        if (parts.length < 3) {
                            out.println("Error: Invalid command format");
                            continue;
                        }

                        double A = Double.parseDouble(parts[0]);
                        double B = Double.parseDouble(parts[1]);
                        String type = parts[2];

                        String result = processCommand(A, B, type);
                        // System.out.println("Instance " + port + ": Sending result '" + result + "'");
                        out.println(result);
                    }
                } catch (IOException | NumberFormatException e) {
                    System.err.println("Instance " + port + ": Error " + e.getMessage());
                }
            }
        } catch (IOException e) {
            System.err.println("Could not start server on port " + port);
            e.printStackTrace();
        }
    }

    private String processCommand(double A, double B, String type) {
        switch (type) {
            case "+":
                return String.valueOf(A + B);
            case "-":
                return String.valueOf(A - B);
            case "*":
                return String.valueOf(A * B);
            case "/":
                if (B != 0) {
                    return String.valueOf(A / B);
                } else {
                    return "Error: Division by zero";
                }
            default:
                return "Error: Unknown command type";
        }
    }

    public static void main(String[] args) {
        if (args.length < 1) {
            System.err.println("Usage: java Instance <port>");
            System.exit(1);
        }

        int port = Integer.parseInt(args[0]);
        Instance instance = new Instance(port);
        new Thread(instance).start();
    }
}

