package org.galaxio.performance.metrics.cases

import io.gatling.http.Predef._
import io.gatling.core.Predef._

object HttpActions {

  val crocodiles = http("GET /public/crocodiles/")
    .get("/public/crocodiles/")
    .check(status is 200)

}
