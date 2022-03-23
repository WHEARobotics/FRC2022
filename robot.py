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

        #set the sensor position to 0
        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)

        #have back motors follow front motor movement
        self.l_motorBack.follow(self.l_motorFront)
        self.r_motorBack.follow(self.r_motorFront)
 
        #have the back motors inverted. might need to invert based on placement
        self.l_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)
        self.r_motorBack.setInverted(ctre._ctre.InvertType.FollowMaster)

        #set mode to coast, meaning that the back-emf will not be generated (back electromotive force)
        self.l_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.l_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorBack.setNeutralMode(ctre._ctre.NeutralMode.Coast)
        self.r_motorFront.setNeutralMode(ctre._ctre.NeutralMode.Coast)                                                                                                                                                                                              
      
        kTimeout = 30 #amount of milliseconds before an error pops up
        kLoop = 0
            
        self.targetVelocity = #int(velocity)
        self.targetVelocity2 = #might not need this controlled loop

        TG1 = #float of calculated constant

        #following motors may or may not be inverted - need to know                                     

        #code for the shooter component
        self.shooter = ctre.TalonFX(5)
        self.shooter.setInverted(True)
        self.shooter.set(ctre._ctre.ControlMode.PercentOutput, 0.0) #motor has a sensor to let it know that it doesn't do anything yet

        #sets the sensor as the one built-in to the falcon's talonfx
        self.shooter.configSelectedFeedbackSensor(ctre._ctre.FeedbackDevice.IntegratedSensor)
        self.shooter.setSelectedSensorPosition(0)

        self.shooter.configNominalOutputForward(0, kTimeout)
        self.shooter.configNominalOutputReverse(0, kTimeout)
        self.shooter.configPeakOutputForward(1, kTimeout)
        self.shooter.configPeakOutputReverse(-1, kTimeout)

        self.shooter.config_kF(kLoop, TG1, kTimeout)
        self.shooter.config_kP(kLoop, 3, kTimeout)
        self.shooter.config_kI(kLoop, 0, kTimeout)
        self.shooter.config_kD(kLoop, 0, kTimeout)

        self.ourTimer = wpilib.Timer()

        #code for the kicker component
        self.kicker = ctre.TalonSRX(6)
        self.kicker.setInverted(True)
        self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

        #code for the tread component
        self.tread = ctre.TalonSRX(7)
        self.tread.setInverted(True)
        self.tread.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

        #code for the collector component
        self.collector = ctre.TalonSRX(8)
        self.collector.setInverted(True)  
        self.collector.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
 
        #set up joysticks
        self.l_joy = wpilib.Joystick(0)
        self.r_joy = wpilib.Joystick(1)


    def autonomousInit(self):

        self.l_motorFront.setSelectedSensorPosition(0)
        self.r_motorFront.setSelectedSensorPosition(0)

    def autonomousPeriodic(self):

        Time = self.ourTimer.get() #sets a timer
 
        l_encoderPos = self.l_motorFront.getSelectedSensorPosition() #get the positions for sensors inside the motor
        r_encoderPos = self.r_motorFront.getSelectedSensorPosition()

    def disabledInit(self):

        #this function gets called once when the robot is disabled. in the past, we have not used this function, but it could occasionally be useful. in this case, we reset some SmartDashboard values
        wpilib.SmartDashboard.putString('DB/String 0',"")
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

        l_encoderPos = self.l_motorFront.getSelectedSensorPosition
        r_encoderPos = self.r_motorFront.getSelectedSensorPosition

        #these are used to tell us where the robot is
        wpilib.SmartDashboard.putString('DB/String 0', 'x:   {:5.3f}'.format(self.left_command.geRawAxis()))
        wpilib.SmartDashboard.putString('DB/String 1', 'y: {:5.3f}'.format(self.right_command.getRawAxis()))
        wpilib.SmartDashboard.putString('DB/String 2', 'z:  {:5.3f}'.format(self.Ljoy.getZ()))
        wpilib.SmartDashboard.putString('DB/String 3', 'Angle: {:5.1f}'.format(self.gyro.getAngle()))

if __name__ == "__main__":
    wpilib.run(MyRobot)