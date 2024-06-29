package org.galaxio.performance.metrics

import io.gatling.core.Predef._
import org.galaxio.gatling.config.SimulationConfig._
import org.galaxio.performance.metrics.scenarios._

class Load extends Simulation {

  setUp(
    HttpScenario().inject(
      rampUsersPerSec(0) to intensity during rampDuration,
      constantUsersPerSec(intensity) during stageDuration,
    ),
  ).protocols(httpProtocol)
    .maxDuration(testDuration)

}
