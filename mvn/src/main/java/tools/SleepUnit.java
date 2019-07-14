package tools;

import java.util.concurrent.TimeUnit;


// 枚举类型中每一个都是一个实例，而不是类
public enum SleepUnit {

    SECOND(SleepUnit.SECOND_SCALE),
    MILLISSECONDS(SleepUnit.MILLI_SCALE),
    MICROSECONDS(SleepUnit.MICRO_SCALE),
    NANOSECONDS(SleepUnit.NANO_SCALE);

    private static final int NANO_SCALE   = 1;
    private static final int MICRO_SCALE  = 2;
    private static final int MILLI_SCALE  = 3;
    private static final int SECOND_SCALE = 4;

    private final int scale;
    private SleepUnit(int scale){
        this.scale = scale;
    }

    public void sleep(long timeout){
        if(timeout > 0){
            try{
                switch (this.scale){
                    case SECOND_SCALE:
                        TimeUnit.SECONDS.sleep(timeout);
                        break;
                    case MILLI_SCALE:
                        TimeUnit.MILLISECONDS.sleep(timeout);
                        break;
                    case MICRO_SCALE:
                        TimeUnit.MICROSECONDS.sleep(timeout);
                        break;
                    case NANO_SCALE:
                        TimeUnit.NANOSECONDS.sleep(timeout);
                        break;
                    default:
                        throw new Exception("invalid scale");
                }

            } catch (Exception e){

            }
        }
    }

    public static void main(String[] args) {
        SleepUnit.MILLISSECONDS.sleep(10);
    }

}
