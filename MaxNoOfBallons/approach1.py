class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character,Integer> map=new HashMap<>();
        char[] s = {'b','a','l','l','o','o','n'};
        int ans=0;
        for(char i:text.toCharArray()){
            map.put(i,map.getOrDefault(i,0)+1);
        }
        outer:
        while(true){
            for(int i=0;i<s.length;i++){
                if(!map.containsKey(s[i])){
                    break outer;
                }
                else {
            if(map.get(s[i])<1){
                break outer;
            } else {
                map.put(s[i],map.get(s[i])-1);
            }
                    
                }
            
        
            }
            ans++;
            
            
        }
        return ans;
    }
}