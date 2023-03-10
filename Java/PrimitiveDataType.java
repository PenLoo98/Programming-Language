public class PrimitiveDataType{
    public static void main(String[] args){
        // 타입 변수명 = 값;
        // byte, short, int, long, float, double, char, boolean

        // 정수형
        byte b = 127;
        short s = 32767;
        int i = 2147483647;
        // long값을 적을때는 뒤에 소문자 l이나 대문자 L을 적어야 합니다.
        long l = 9223372036854775807L;

        // 실수형
        // float에 값을 대입할 때는 실수 뒤에 소문자 f나 대문자 F를 붙여야 합니다.
        float f = 3.14F;
        double d = 3.14;

        // 문자형
        char character = 'A';

        // 논리형
        boolean isTrue = true;

        System.out.println("byte b = "+b);
        System.out.println("short s = "+s);
        System.out.println("int i = "+i);
        System.out.println("long l = "+l);

        System.out.println("float f = "+f);
        System.out.println("double d = "+d);

        System.out.println("char character = "+character);

        System.out.println("boolean isTrue = "+isTrue);
    }
    
}
