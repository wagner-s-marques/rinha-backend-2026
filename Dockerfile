FROM clojure:temurin-21-lein AS build
WORKDIR /app
COPY project.clj .
RUN lein deps
COPY src src
RUN lein uberjar

FROM eclipse-temurin:21-jre-alpine
WORKDIR /app
COPY --from=build /app/target/app.jar app.jar
EXPOSE 3000
CMD ["java", "-jar", "app.jar"]
