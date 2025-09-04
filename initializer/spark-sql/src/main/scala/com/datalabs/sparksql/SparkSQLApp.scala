import org.apache.spark.sql.SparkSession

object SparkSQLApp {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder.appName("SparkSQLApp").getOrCreate()
    val df = spark.read.json("examples/src/main/resources/people.json")
    df.createOrReplaceTempView("people")
    spark.sql("SELECT name, age FROM people WHERE age > 21").show()
  }
}
