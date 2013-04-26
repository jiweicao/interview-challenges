import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.SortedMap;
import java.util.TreeMap;
/*
Solutino by jiweicao

Challenge Description:

Credits: This challenge was contributed by Sam McCoy

Given a string S, and a list of strings of positive length, F1,R1,F2,R2,...,FN,RN, proceed to find in order the occurrences (left-to-right) of Fi in S and replace them with Ri. All strings are over alphabet { 0, 1 }. Searching should consider only contiguous pieces of S that have not been subject to replacements on prior iterations. An iteration of the algorithm should not write over any previous replacement by the algorithm.

Input sample:

Your program should accept as its first argument a path to a filename. Each line in this file is one test case. Each test case will contain a string, then a semicolon and then a list of comma separated strings.eg.

10011011001;0110,1001,1001,0,10,11
Output sample:

For each line of input, print out the string after substitutions have been made.eg.

11100110

*/
public class Solution {
    public static void main (String[] args) throws IOException {
	File file = new File("test.txt");
	@SuppressWarnings("resource")
	    BufferedReader inFile = new BufferedReader(new FileReader(file));
	String line;
	while ((line = inFile.readLine()) != null) {
	    String[] lineArray = line.split("[;,]");
	    if (lineArray.length > 0) {
		String oldString = lineArray[0];
		SortedMap<Integer, Integer> substitutionMap = new TreeMap<Integer, Integer>();
		SortedMap<Integer, Integer> indexMap = new TreeMap<Integer, Integer>();
		SortedMap<Integer, Integer> storeMap = new TreeMap<Integer, Integer>();
		indexMap.put(0, oldString.length());
		    
		for(int i=1; i<lineArray.length; i+=2) {
		    for (int start: indexMap.keySet()) {
			int end = indexMap.get(start);
			int left = start + oldString.substring(start, end).indexOf(lineArray[i]);
			if (left != -1) {
			    int right = left + lineArray[i].length();
			    storeMap.put(left, right);
			    substitutionMap.put(left, i+1);
			    if(left == start) {
				indexMap.remove(start);
			    }
			    else {
				indexMap.put(start, left);
			    }
			    if(right < end)
				indexMap.put(right, end);
			    break;
			}
		    }
		}
		
		for (int start: indexMap.keySet()) {
		    storeMap.put(start, indexMap.get(start));
		}
		
		String resultString = new String();
		for (int start: storeMap.keySet()) {
		    if(substitutionMap.containsKey(start)) {
			resultString += lineArray[substitutionMap.get(start)];
		    }
		    else {
			resultString  += oldString.substring(start, storeMap.get(start));
		    }
		}
		System.out.println(resultString);
	    }
	}
    }
}