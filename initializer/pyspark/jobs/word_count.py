from pyspark import SparkContext

sc = SparkContext("local", "WordCount")
text = sc.textFile("README.md")
counts = text.flatMap(lambda line: line.split(" ")) //             .map(lambda word: (word, 1)) //             .reduceByKey(lambda a, b: a + b)
print(counts.collect())
