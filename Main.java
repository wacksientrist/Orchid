import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        int numNodes = Integer.parseInt(args[0]); // Number of nodes to create
        int startingPort = 8001; // Starting port number, can be adjusted as needed

        for (int i = 1; i <= numNodes; i++) {
            final int nodeId = i;
            final int port = startingPort + nodeId - 1;
            Thread thread = new Thread(() -> {
                try {
                    runInstance(port);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            thread.start();
        }
    }

    private static void runInstance(int port) throws IOException {
        Instance instance = new Instance(port);
        instance.run();
    }
}
