/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package kmeans;
import java.util.*;
import java.nio.file.*;
import java.io.*;
import java.lang.*;

/**
 *
 * @author Nur
 */
public class Kmeans {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner scan = new Scanner(System.in);
        
        String fileName = "/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment02/Track1/gene.txt";

        // This will reference one line at a time
        String line = null;
        List<String> lines = new ArrayList<String>();
        List<Integer> intList = new ArrayList<Integer>();;
        
        
        try {
            // FileReader reads text files in the default encoding.
            FileReader fileReader = 
                new FileReader(fileName);

            // Always wrap FileReader in BufferedReader.
            BufferedReader bufferedReader = 
                new BufferedReader(fileReader);

            while((line = bufferedReader.readLine()) != null) {
                System.out.println(line);
                lines.add(line);
                
            }
            String[] stringArray = lines.toArray(new String[lines.size()]);
            // Always close files.
            int[] numbers = new int[stringArray.length];
            for(int i = 0;i < stringArray.length;i++) {
                try {
                    numbers[i] = Integer.parseInt(stringArray[i]);
                } catch (NumberFormatException nfe) {};
                
            }
            
            bufferedReader.close();            
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                "Unable to open file '" + 
                fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println(
                "Error reading file '" 
                + fileName + "'");                   
            // Or we could just do this: 
            // ex.printStackTrace();
        }
        
            
        
        /*
        
        List<Integer> integers = new ArrayList<Integer>();    
        Scanner fileScanner = new Scanner(new File("/Users/Nur/Documents/Spring_2015/Data_Mining/Assignment02/Track1.txt"));
        while (fileScanner.hasNextInt()){
            integers.add(fileScanner.nextInt());
        }
        System.out.println(integers);
        
        byte[] fileArray;
        //fileArray = Files.readAllBytes(file);


        int k = scan.nextInt();
        int[] numClust = new int[k];
                */
        
    }
    
}
