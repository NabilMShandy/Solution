class sumOfArray{
    static int sum0fArr(int num){
        num = Math.abs(num);
        char[] charNum = String.valueOf(num).toCharArray();
        int arrNum[] = new int[charNum.length];
        int sum = 0;

        for(int i=0; i < charNum.length; i++){
            arrNum[i] = Character.getNumericValue(charNum[i]);
            sum+=arrNum[i];
        }
        return sum;
    }

    public static void main(String[] args) {
        System.out.println(sum0fArr(-9082));
    }
}