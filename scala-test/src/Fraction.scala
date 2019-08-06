// 隐式转换

import scala.language.implicitConversions // 声明使用隐式转换

class Fraction (n: Int, d:Int){
  private val num = n
  private val den = d

  def * (other: Fraction) = new Fraction(num * other.num, den * other.den).getResult // 自定义操作符

  def getResult = {
    num * den
  }
}

object Fraction{
  implicit def int2Fraction(n: Int) = new Fraction(n, 1)  // 在伴生对象中设置隐式转换

  def main(args: Array[String]): Unit = { // main函数
    val result =  3 * (new Fraction(4,5))
    println(result)
  }
}
