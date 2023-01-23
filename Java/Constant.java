public class Constant {
    public static void main(String[] args) {
        // 상수에는 한 번만 값 할당이 가능, 이후에는 수정불가
        // 상수면서 int타입인 FREEZE라는 이름의 상수 선언
        final int FREEZE;
        FREEZE = 0;
        System.out.println("FREEZE == "+FREEZE+"℃");

        // 상수명명 관례는 대문자로 구성된 명사, 2단어 이상이면 _(언더바)로 구분
        final int LIGHT_SPEED;
        LIGHT_SPEED = 299792458;
        System.out.println("LIGHT_SPEED == "+LIGHT_SPEED+"m/s");
    }
}
