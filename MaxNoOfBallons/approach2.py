class Solution {
    public int maxNumberOfBalloons(String text) {
        HashMap<Character,Integer> map=new HashMap<>();
        char[] s = {'b','a','l','l','o','o','n'};
        int ans=Integer.MAX_VALUE;
        
        
        for(char i:text.toCharArray()){
            map.put(i,map.getOrDefault(i,0)+1);
        
        }
        if(!(map.containsKey('l') || map.containsKey('o'))){
            return 0;
        } else {
            int f=map.getOrDefault('l',0)/2;
        int g=map.getOrDefault('o',0)/2;
        map.put('l',f);
        map.put('o',g);
        }
        
    
        for(int i=0;i<s.length;i++){
            if(!map.containsKey(s[i])){
                return 0;
            } else {
                
                if(map.get(s[i])<ans){
                    ans=map.get(s[i]);
                }
            }
        }
        
        if(ans==Integer.MAX_VALUE){
            return 0;
        }
        return ans;
        }
}