# !/usr/bin/env python3
"""
robot code for FRC 2022
"""
import wpilib
import ctre
import wpilib.drive

class MyRobot(wpilib.TimedRobot):

    def robotInit(self):

         # set up drive train motor controllers, Falcon 500 using TalonFX
        self.l_motorBack = ctre.TalonFX(1)
        self.l_motorBack.setInverted(True)
 
        self.r_motorBack = ctre.TalonFX(2)
 
        self.l_motorFront = ctre.TalonFX(3)
        self.l_motorFront.setInverted(True)
 
        self.r_motorFront = ctre.TalonFX(4)
      
        #have back motors follow front motor movement
        self.l_motorBack.follow(self.l_motorFront)
        self.r_motorBack.follow(self.r_motorFront)
 
        #have the back motors inverted
        self.l_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)
        self.r_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)

        #set mode to coast 
        self.l_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.l_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)
 
        #set up joysticks
        self.l_joy = wpilib.Joystick(0)
        self.r_joy = wpilib.Joystick(1)

        #set the sensor position to 0
        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)

    def autonomousInit(self):

        #set sensor position to 0
        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)

    def autonomousPeriodic(self):

        #set up a timer
        Time = self.ourTimer.get()
 
        l_encoderPos = self.l_motorFront.getSelectedSensorPosition()
        r_encoderPos = self.r_motorFront.getSelectedSensorPosition()

    def disabledInit(self):

        #this function gets called once when the robot is disabled. in the past, we have not used this function, but it could occasionally be useful. in this case, we reset some SmartDashboard values
        wpilib.SmartDashboard.putString('DB/String 0',")
        wpilib.SmartDashboard.putNumber('DB/SLider 0', 0)
        wpilib.SmartDashboard.putBoolean('DB/LED 0', False)

    def teleopInit(self):

        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)
 
    def teleopPeriodic(self):

        #get joystick values
        left_command = self.l_joy.getRawAxis(1)
        right_command = self.r_joy.getRawAxis(1)
 
        #get the output of the motors in percentage 
        self.l_motorFront.set(ctre._ctre.ControlMode.PercentOutput, left_command)
        self.r_motorFront.set(ctre._ctre.ControlMode.PercentOutput, right_command)

        l_encoderPos = self.l_motorFront.getSelectedSensorPosition #TO DO-STUDENT: there needs to be one more thing added at the end of these "methods" so we can plug in parameters if needed
        r_encoderPos = self.r_motorFront.getSelectedSensorPosition


        #TO DO STUDENT: modify our smart dashboard outputs so we get values from both our joysticks, and we see what sensor position each drive motors are at
        wpilib.SmartDashboard.putString('DB/String 0', 'x:   {:5.3f}'.format(self.Ljoy.getX()))
        wpilib.SmartDashboard.putString('DB/String 1', 'y: {:5.3f}'.format(self.Ljoy.getY()))
        wpilib.SmartDashboard.putString('DB/String 2', 'z:  {:5.3f}'.format(self.Ljoy.getZ()))
        wpilib.SmartDashboard.putString('DB/String 3', 'Angle: {:5.1f}'.format(self.gyro.getAngle()))

if __name__ == "__main__":
    wpilib.run(MyRobot)