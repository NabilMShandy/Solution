public class Maskify {
    public static String maskify(String str) {
        int sign = 0;
        int searched_index = 0;

        for(int i = str.length()-1; i > -1; i--){
            sign++;

            if(sign == 4){
                searched_index = i;
                break;
            }
        }
      
        String maskify = "";
      
        for(int j = 0; j < str.length()-4; j++){
            maskify+="#";
        }
        for(int k = searched_index; k < str.length(); k++){
            maskify+=str.charAt(k);
        }
        return maskify;
    }
}