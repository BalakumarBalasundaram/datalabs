![alt text](image.png)

![alt text](image-1.png)

![alt text](image-2.png)

# Error
![alt text](image-3.png)
 
 Go to project -> settings ->  Build, execution, deployment -> Gradle -> Gradle JVM -> change to 17

# Questions
1) why gradle JVM is important?
Gradle JVM is the version of Java that Gradle uses to run the build. It is not the version of Java that your project uses. The version of Java that your project uses is determined by the sourceCompatibility and targetCompatibility settings in your build.gradle file.
2) What is the difference between sourceCompatibility and targetCompatibility?
sourceCompatibility is the version of Java that the source code is compatible with. targetCompatibility is the version of Java that the compiled code is compatible with. The compiled code will be compatible with the version of Java specified by targetCompatibility and all earlier versions of Java. If you are using a version of Java that is later than the version specified by targetCompatibility, you may get warnings about using features that are not available in the target version of Java.
3) What is project settings Language level?
The language level is the version of the Java language that the project uses. The language level determines which features of the Java language are available to you. For example, if you set the language level to Java 8, you will not be able to use features that were introduced in Java 9 or later. The language level is set in the project settings in IntelliJ IDEA.
4) What is the difference between project settings Language level and sourceCompatibility?
The language level is the version of the Java language that the project uses. The sourceCompatibility is the version of Java that the source code is compatible with. The sourceCompatibility setting is used by the Java compiler to determine which features of the Java language are available to you. If you set the sourceCompatibility to Java 8, you will not be able to use features that were introduced in Java 9 or later, even if the language level is set to Java 9 or later. The language level is set in the project settings in IntelliJ IDEA, while the sourceCompatibility is set in the build.gradle file.
5) did sourceCompatibility and project settings Language level are functionally same?
The sourceCompatibility setting in the build.gradle file and the language level setting in the project settings in IntelliJ IDEA are functionally the same. They both determine the version of the Java language that the source code is compatible with. However, the sourceCompatibility setting in the build.gradle file takes precedence over the language level setting in the project settings. If the sourceCompatibility setting is set to Java 8 in the build.gradle file, you will not be able to use features that were introduced in Java 9 or later, even if the language level is set to Java 9 or later in the project settings.





# Udemy
https://www.udemy.com/course/code-graphql-application-with-java-spring-boot-netflix-dgs/learn/lecture/36109354#overview