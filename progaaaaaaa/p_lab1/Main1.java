class Main1 {
    public static void main (String [] args){
        short[] I;
        I = new short[8];
        for (int i = 0; i< I.length;i++){
            I[i] = (short)(19 - i*2);
        }
        double[] x = new double[18];
        int minValue = -5;
        int maxValue = 5;
        for (int i = 0; i < x.length; i++) {
            x[i] = Math.random() * (maxValue - minValue) + minValue;
        }

        double [][] s = new double[8][18];
        for (int i = 0;i<8;i++){
            for (int j = 0; j<18; j++){
                calculate(i,j, I, x, s);
            }
        }
        printArr(8,18,s);
    }

    public static void calculate(int i,int j, short[] I, double[] x, double[][] s) {
        if (I[i] == 19) {
            s[i][j] = calculate1(x[j]);
        } else if ((I[i] == 5)|| (I[i] == 7)|| (I[i] == 13)|| (I[i] == 17)){
            s[i][j] = calculate2(x[j]);
        } else {
            s[i][j] = calculate3(x[j]);
        }
    }

    public static double calculate1(double x){
        return Math.asin(0.5*Math.pow(x*Math.E+1, 2));
    }

    public static double calculate2(double x){
        return Math.asin(Math.pow(Math.sin(x), 2));
    }

    public static double calculate3(double x){
        double value1 = Math.log(Math.abs(x));
        double value2 = Math.cbrt(x)/(Math.tan(x)-3);
        double value3 = (Math.pow(4/(Math.pow(x,(x+1)/x) - 1), 3) +0.5)/3;
        return Math.pow(Math.E, Math.pow(value3, Math.pow(value2, value1)));
    }

    public static void print(double value) {
        if (Double.isNaN(value)) {
            System.out.print("     NaN");
        } else if (Double.isInfinite(value)) {
            System.out.print("     Inf");
        } else {
            System.out.print(String.format("%8.4f", value));
        }
    }

    public static void printArr(int i, int j, double[][] x){
        for (int I = 0;I<i;I++){
            for (int J = 0; J<j; J++){
                print(x[I][J]);
            }
            System.out.println();
        }

    }


}