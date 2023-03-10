public class PrimitiveDataTypeChange {
    public static void main(String[] args) {
        // 기본형 타입변환
        // byte -> short -> int -> long -> float -> double
        // byte, short, char는 연산시 int로 자동형변환

        byte byteValue = 10;
        char charValue = '2';
        int intValue = byteValue * charValue;

        System.out.println("byteValue = "+byteValue);
        System.out.println("charValue = "+charValue);
        System.out.println("intValue = "+intValue);
        

        // 묵시적 형변환
        int x = 10000;
        long y = x;

        // 명시적 형변환
        long A = 20000;
        int B = (int)A;

        System.out.println("x = "+x);
        System.out.println("y = "+y); 
        System.out.println("A = "+A);
        System.out.println("B = "+B);
    }
    
}
