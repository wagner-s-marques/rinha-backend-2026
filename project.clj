(defproject rinha-backend-2026 "0.1.0-SNAPSHOT"
  :dependencies [[org.clojure/clojure "1.11.1"]
                 [ring/ring-core "1.12.1"]
                 [ring/ring-json "0.5.1"]
                 [http-kit "2.8.0"]
                 [compojure "1.7.1"]
                 [cheshire "5.13.0"]]
  :main rinha-backend-2026.core
  :uberjar-name "app.jar"
  :profiles {:uberjar {:aot :all}})
