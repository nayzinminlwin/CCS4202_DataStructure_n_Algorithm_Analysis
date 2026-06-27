package DynamicProgramming;

import java.util.Arrays;
import java.util.Scanner;

public class KnapsackProblem {

    // 1. Array for item names
    static String[] items;

    // 2. Array for item weights (w)
    static int[] w;

    // 3. Array for importance values (v)
    static int[] v;

    // 4. Maximum vehicle capacity (W)
    static int W;

    public static void main(String[] args) {

        // get inputs from the user
        getInputs();

        // create dummy data for the knapsack problem
        // seedData();

        System.out.println("\nGreedy Algorithm for Knapsack Problem");
        System.out.println("--------------------------------------");
        greedyAlgo(items, w, v, W);

        System.out.println("\nDynamic Programming Algorithm for Knapsack Problem");
        System.out.println("---------------------------------------------------");
        knapsackAlgo(items, w, v, W);

    }

    public static void getInputs() {

        Scanner sc = new Scanner(System.in);

        // Get user inputs for items, weights, values, and capacity
        System.out.print("Please enter the number of items:");

        // Read number of items and initialize arrays accordingly
        int n = sc.nextInt();

        items = new String[n];
        w = new int[n];
        v = new int[n];

        sc.nextLine(); // Consume the newline character after reading the number of items
        for (int i = 0; i < n; i++) {

            System.out.println("Please enter the weight, value, and name for each item:");

            System.out.print("Item " + (i + 1) + " name: ");
            items[i] = sc.nextLine();

            System.out.print("Item " + (i + 1) + " weight: ");
            w[i] = sc.nextInt();

            System.out.print("Item " + (i + 1) + " value: ");
            v[i] = sc.nextInt();

            sc.nextLine(); // Consume the newline character after reading the weight and value
        }

        System.out.print("Please enter the knapsack capacity: ");
        W = sc.nextInt();

        sc.close();
    }

    public static void seedData() {
        items = new String[] { "Medicine kits", "Food packs", "Bottled water", "Blankets", "Flashlights",
                "Hygiene kits" };
        w = new int[] { 6, 5, 5, 4, 2, 1 };
        v = new int[] { 48, 35, 35, 20, 8, 3 };
        W = 10;
    }

    public static void greedyAlgo(String[] items, int[] w, int[] v, int W) {

        // start timer
        long startTime = System.nanoTime();

        // number of items
        int n = w.length;

        // the final knapsack
        int[] knapsack = new int[n];

        // the value to weight ratio
        double[] v2w_ratio = new double[n];
        Integer[] sortedIndexes = new Integer[n];

        for (int i = 0; i <= n - 1; i++) {
            v2w_ratio[i] = (double) v[i] / w[i];
            sortedIndexes[i] = i;
        }

        // Array Sorting
        Arrays.sort(sortedIndexes, (a, b) -> Double.compare(v2w_ratio[b], v2w_ratio[a]));

        // total weight in knapsack
        int currentW = 0;

        // total value
        int totalV = 0;

        // run the greedy knapsack
        for (int i = 0; i <= n - 1; i++) {
            int j = sortedIndexes[i];
            if (currentW + w[j] > W) {
                // skip the item if it exceeds the maximum weight
                continue;
            } else {
                knapsack[i] = j; // add the item to the knapsack
                currentW += w[j]; // update the current weight
                totalV += v[j]; // update the total value

                System.out.printf(
                        "Item %d (%s) is added to the knapsack. \n Current total weight : %d \n Current total value : %d\n",
                        j,
                        items[j], currentW, totalV);
            }
        }

        // stop timer
        long endTime = System.nanoTime();
        System.out.println("Execution time: " + ((endTime - startTime) / 1_000_000_000.0) + " seconds");
        System.out.println("");

    }

    public static void knapsackAlgo(String[] items, int[] w, int[] v, int W) {
        // start timer
        long startTime = System.nanoTime();

        int n = items.length;

        // indexes of the items
        Integer[] indexes = new Integer[n];
        for (int i = 0; i < n; i++) {
            indexes[i] = i;
        }

        // sort the items weight for the algorithm
        Arrays.sort(indexes, (a, b) -> Integer.compare(w[a], w[b]));

        // System.out.println("Sorted indexes by weight: " + Arrays.toString(indexes));

        // final value array for the knapsack
        int[][] finalV = new int[n + 1][W + 1];

        // total weight in the knapsack
        int totalWeight = 0;

        // loop all the items
        for (int i = 1; i <= n; i++) {

            // indexes by sorted weight
            int real_i = indexes[i - 1];

            // loop all the available Weight of knapsack
            for (int j = 0; j <= W; j++) {

                if (w[real_i] > j) {
                    finalV[i][j] = finalV[i - 1][j];
                } else {
                    finalV[i][j] = Math.max(finalV[i - 1][j], v[real_i] + finalV[i - 1][j - w[real_i]]);
                }
            }

        }

        // // print the final value array for the knapsack
        // System.out.println("w , v, itemID, 0 1 2 3 4 5 6 7 8 9 10");
        // System.out.println("0 , 0, item, 0 0 0 0 0 0 0 0 0 0 0");

        // for (int i = 1; i <= n; i++) {
        // System.out.print(w[indexes[i - 1]] + " , " + v[indexes[i - 1]] + " , " +
        // indexes[i - 1] + " , ");
        // for (int j = 0; j <= W; j++) {
        // System.out.print(finalV[i][j] + " ");
        // }
        // System.out.println();
        // }

        // loop from bottom to top until i and j are less than or equal to 0
        for (int i = n, j = W; i > 0 && j > 0; i--) {

            // remove the extra 0 row
            int real_i = indexes[i - 1];

            // check if the item made the value change
            if (finalV[i][j] != finalV[i - 1][j]) {
                System.out.printf("Item %d (%s) is added to the knapsack.%n", real_i, items[real_i]);
                totalWeight += w[real_i]; // update the total weight in the knapsack
                j -= w[real_i]; // update remaining weight to repeat
            }
        }

        // print the maximum value in the knapsack
        System.out.println("Maximum value in Knapsack : " + finalV[n][W]);

        // print total weight in the knapsack
        System.out.println("Total weight in Knapsack : " + totalWeight);

        // stop timer
        long endTime = System.nanoTime();
        System.out.println("Execution time: " + ((endTime - startTime) / 1_000_000_000.0) + " seconds");
    }

}
