#ifndef DRONE_CONTROLLER_H
#define DRONE_CONTROLLER_H

class DroneController {
  public:
    DroneController();
    void moveX(bool right);
    void moveY(bool up);
    void moveZ(bool front);
    void rotX(float rad);
    void rotY(float rad);
    void rotZ(float rad);
    void updateMotion();
    void land();

  private:
    float x;
    float y;
    float z;
    float roll;
    float yaw;
    float pitch;
    const float maxTilt = 10;
};

#endif
