import java.io.IOException;

public class Main {

    public static void main(String[] args) {
        int numNodes = 3; // You can change this to NUM_NODES or pass as an argument

        for (int i = 1; i <= numNodes; i++) {
            final int nodeId = i;
            Thread thread = new Thread(() -> {
                try {
                    runInstance(nodeId);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });
            thread.start();
        }
    }

    private static void runInstance(int nodeId) throws IOException {
        Instance instance = new Instance(nodeId);
        instance.run();
    }
}
