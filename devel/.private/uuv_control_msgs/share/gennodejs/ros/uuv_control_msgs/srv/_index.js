
"use strict";

let InitCircularTrajectory = require('./InitCircularTrajectory.js')
let ResetController = require('./ResetController.js')
let GetMBSMControllerParams = require('./GetMBSMControllerParams.js')
let InitHelicalTrajectory = require('./InitHelicalTrajectory.js')
let GetWaypoints = require('./GetWaypoints.js')
let SetMBSMControllerParams = require('./SetMBSMControllerParams.js')
let IsRunningTrajectory = require('./IsRunningTrajectory.js')
let InitWaypointSet = require('./InitWaypointSet.js')
let SwitchToManual = require('./SwitchToManual.js')
let AddWaypoint = require('./AddWaypoint.js')
let GoToIncremental = require('./GoToIncremental.js')
let SetPIDParams = require('./SetPIDParams.js')
let StartTrajectory = require('./StartTrajectory.js')
let Hold = require('./Hold.js')
let GetSMControllerParams = require('./GetSMControllerParams.js')
let InitRectTrajectory = require('./InitRectTrajectory.js')
let GetPIDParams = require('./GetPIDParams.js')
let GoTo = require('./GoTo.js')
let SwitchToAutomatic = require('./SwitchToAutomatic.js')
let SetSMControllerParams = require('./SetSMControllerParams.js')
let ClearWaypoints = require('./ClearWaypoints.js')
let InitWaypointsFromFile = require('./InitWaypointsFromFile.js')

module.exports = {
  InitCircularTrajectory: InitCircularTrajectory,
  ResetController: ResetController,
  GetMBSMControllerParams: GetMBSMControllerParams,
  InitHelicalTrajectory: InitHelicalTrajectory,
  GetWaypoints: GetWaypoints,
  SetMBSMControllerParams: SetMBSMControllerParams,
  IsRunningTrajectory: IsRunningTrajectory,
  InitWaypointSet: InitWaypointSet,
  SwitchToManual: SwitchToManual,
  AddWaypoint: AddWaypoint,
  GoToIncremental: GoToIncremental,
  SetPIDParams: SetPIDParams,
  StartTrajectory: StartTrajectory,
  Hold: Hold,
  GetSMControllerParams: GetSMControllerParams,
  InitRectTrajectory: InitRectTrajectory,
  GetPIDParams: GetPIDParams,
  GoTo: GoTo,
  SwitchToAutomatic: SwitchToAutomatic,
  SetSMControllerParams: SetSMControllerParams,
  ClearWaypoints: ClearWaypoints,
  InitWaypointsFromFile: InitWaypointsFromFile,
};
