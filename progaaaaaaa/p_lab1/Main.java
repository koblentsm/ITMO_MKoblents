class Main {
    public static void main (String [] args){
        short[] I;
        I = new short[8];
        for (int i = 0; i< I.length;i++){
            I[i] = (short)(19 - i*2);
        }
        double[] x;
        x = new double[18];
        int minValue = -5;
        int maxValue = 5;
        for (int i = 0; i < x.length; i++) {
            x[i] = Math.random() * (maxValue - minValue) + minValue;
        }

        double [][] s;
        s = new double[8][18];
        for (int i = 0;i<8;i++){
            for (int j = 0; j<18; j++){
                counter(i,j, I, x, s);
            }
        }
        printArr(8,18,s);


    }
    public static void counter(int i,int j, short[] I, double[] x, double[][] s) {
        double X = x[j];
        short Ii = I[i];
        if (Ii == 19) {
            s[i][j] = Math.asin(0.5*Math.pow(X*Math.E+1, 2));
        } else if ((Ii == 5)|| (Ii == 7)|| (Ii == 13)|| (Ii == 17)){
            s[i][j] = Math.asin(Math.pow(Math.sin(X), 2));
        } else {
            double value1;
            value1 = Math.log(Math.abs(X));
            double value2;
            value2 = Math.cbrt(X)/(Math.tan(X)-3);
            double value3;
            value3 = (Math.pow(4/(Math.pow(X,(X+1)/X) - 1), 3) +0.5)/3;
            s[i][j] = Math.pow(Math.E, Math.pow(value3, Math.pow(value2, value1)));
        }
    }

    public static void print(double value) {
        if (Double.isNaN(value)) {
            System.out.print("       NaN");
        } else if (Double.isInfinite(value)) {
            System.out.print("       Inf");
        } else {
            System.out.print(String.format("%10.4f", value));
        }
    }

    public static void printArr(int i, int j, double[][] x){
        for (int I = 0;I<i;I++){
            for (int J = 0; J<j; J++){
                print(x[I][J]);
            }
            System.out.println("\n");
        }

    }


}