import Dependencies._

enablePlugins(GatlingPlugin)

lazy val root = (project in file("."))
  .settings(
    inThisBuild(
      List(
        organization := "org.galaxio.performance",
        scalaVersion := "3.8.0",
        version      := "0.1.0",
      ),
    ),
    name := "metrics",
    libraryDependencies ++= gatling,
    libraryDependencies ++= gatlingPicatinny,
      scalacOptions ++= Seq (
        "-encoding",
        "UTF-8",
        "-Xfatal-warnings",
        "-deprecation",
        "-feature",
        "-unchecked",
        "-language:implicitConversions",
        "-language:higherKinds",
        "-language:existentials",
        "-language:postfixOps"
      ),
  )
