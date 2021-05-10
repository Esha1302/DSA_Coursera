import java.util.*;
public class MaximumPairwiseProduct {

	public static void main(String[] args) {
//		System.out.println("Enter N = ");
		Scanner kb = new Scanner(System.in);
		int n = kb.nextInt();
		long arr[] = new long[n];
		for(int i=0;i<n;i++) {
			arr[i] = kb.nextLong();
		}
		int max_index_1 = 0;
		int max_index_2 = 0;
		for(int i=0;i<n;i++) {
			if(arr[i]>arr[max_index_1]) 
				max_index_1 = i;

		}
		long t = arr[max_index_1];
		arr[max_index_1] = arr[n-1];
		arr[n-1] = t;
		
		
		for(int j=0;j<n-1;j++) {
			if(arr[j]>arr[max_index_2])
				max_index_2 = j;
		}

		System.out.println(t*arr[max_index_2]);
	}

}
