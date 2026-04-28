public class Solution {
    public string CountAndSay(int n) {
        
        if (n==1)
         return "1";
        string res="1";
        for(int i=1;i<n;i++){
            StringBuilder nextString = new StringBuilder();
            int j=0;
            while(j < res.Length){
             int  count=0;
             char say=res[j];
            while(j < res.Length &&say==res[j]){
               count++;
               j++;
            }
            nextString.Append(count);
            nextString.Append(say);
            }
             res=nextString.ToString();
        }
        return res;
    }
}