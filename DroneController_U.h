#ifndef DRONE_CONTROLLER_U
#define DRONE_CONTROLLER_U

DroneController::DroneController(){
  instance = this;
}

static DroneController DroneController::getInstance() {
  if (instance == 0) {
    instance = &DroneController();
  }
  return instance;
}

void DroneController::moveX(bool right) {
  this->x += right ? 1 : -1;
}

void DroneController::moveY(bool up) {
  this->y += up ? 1 : -1;
}

void DroneController::moveZ(bool front) {
  this->z += front ? 1 : -1;
}

void DroneController::rotX(float rad) {
  this->roll += rad;
  if (this->roll > this->maxTilt) {
    this->roll = this->maxTilt;
  } else if (this->roll < -this->maxTilt) {
    this->roll = -this->maxTilt;
  }
}

void DroneController::rotY(float rad) {
  this->yaw += rad;
  if (this->yaw > this->maxTilt) {
    this->yaw = this->maxTilt;
  } else if (this->yaw < -this->maxTilt) {
    this->yaw = -this->maxTilt;
  }
}

void DroneController:rotZ(float rad) {
  this->pitch += rad;
  if (this->pitch > this->maxTilt) {
    this->pitch = this->maxTilt;
  } else if (this->pitch < -this->maxTilt) {
    this->pitch = -this->maxTilt;
  }
}

void DroneController::updateMotion() {
//  speed up or slow down motors
}

void DroneController::land() {
  while (this->y > 0) {
    DroneController::moveY(false);
    DroneController::updateMotion();
    delay(500);
  }
}

#endif
