public class Solution {
    public void sortColors(int[] A) {
        int i=0, j=A.length-1, temp=0;
        while (i < A.length && A[i] == 0) {
        	i++;
        }
        while (j >= 0 && A[j] == 2) {
        	j--;
        }
        for (int k = i; k <= j; ++k)
        {
        	if (A[k] == 0) {
        		temp = A[i];
        		A[i] = A[k];
        		A[k] = temp;
        		while (A[i] == 0) {
        			i++;
        		}
	        	if (A[k] == 2) {
	        		temp = A[j];
	        		A[j] = A[k];
	        		A[k] = temp;
	        		while (A[j] == 2) {
	        			j--;
	        		}
	        	}
        	}
        	if (A[k] == 2) {
        		temp = A[j];
        		A[j] = A[k];
        		A[k] = temp;
        		while (A[j] == 2) {
        			j--;
        		}
        		if (A[k] == 0) {
        			temp = A[i];
        			A[i] = A[k];
        			A[k] = temp;
        			while (A[i] == 0) {
        				i++;
        			}
        		}
        	}
        	if (k < i) {
        		k = i;
        	}
        }        
    }
}
