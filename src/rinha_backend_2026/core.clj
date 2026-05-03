(ns rinha-backend-2026.core
  (:require [compojure.core :refer [defroutes GET POST]]
            [ring.middleware.json :refer [wrap-json-body wrap-json-response]]
            [org.httpkit.server :refer [run-server]]
            [rinha-backend-2026.controllers.fraud-score :as fraud-score])
  (:gen-class))

(defroutes routes
  (GET "/status" [] {:status 204 :body ""})
  (GET "/ready" [] {:status 200 :body "Up and Running"})
  (POST "/fraud-score" {body :body} {:status 200 :body (fraud-score/score body)}))

(def app
  (-> routes
      (wrap-json-body {:keywords? true})
      wrap-json-response))

(defn -main [& _]
  (run-server app {:port 3000})
  @(promise))
