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
        self.l_motorBack = ctre.TalonFX(4) #this is #4, it was 1
        self.l_motorBack.setInverted(True)
 
        self.r_motorBack = ctre.TalonFX(1) #this is #1, it wasv 2

        self.l_motorFront = ctre.TalonFX(3) #this is #3, it was 3
        self.l_motorFront.setInverted(True)
 
        self.r_motorFront = ctre.TalonFX(2) #this is #2, it was 4

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

        self.l_motorEncodePos = self.l_motorBack.getSelectedSensorPosition
        self.r_motorEncodePos = self.r_motorBack.getSelectedSensorPosition


        '''SHOOTER initialization code'''

        kTimeout = 30 #amount of milliseconds before an error pops up
        kLoop = 0
            
        self.targetVelocity = int(11000)
        #self.targetVelocity2 = #might not need this controlled loop

        TG1 = 767.25 / self.targetVelocity  ##3/29: added this back in

        #following motors may or may not be inverted - need to know                                     

        #code for the shooter component
        self.shooter = ctre.TalonFX(6) ##3/20: changed from 5 to 6
        self.shooter.setInverted(True) ##3/29- this was true, but because of the jumping back and forth, I set it to false.  NOthing changed
        #self.shooter.set(ctre._ctre.ControlMode.PercentOutput, 0.0) #motor has a sensor to let it know that it doesn't do anything yet 
        #tried commenting above out.        

        #sets the sensor as the one built-in to the falcon's talonfx
        #self.shooter.configSelectedFeedbackSensor(ctre._ctre.FeedbackDevice.IntegratedSensor)
        self.shooter.setSelectedSensorPosition(0)

        #set mode to coast, meaning that the back-emf will not be generated (back electromotive force)
        self.shooter.setNeutralMode(ctre._ctre.NeutralMode.Coast)

        #set up variables equal to encoder positions
        self.shooterEncodePos = self.shooter.getSelectedSensorPosition()

        self.shooter.configNominalOutputForward(0, kTimeout)
        self.shooter.configNominalOutputReverse(0, kTimeout)
        self.shooter.configPeakOutputForward(1, kTimeout)
        self.shooter.configPeakOutputReverse(-1, kTimeout)

        self.shooter.config_kF(kLoop, TG1, kTimeout) #NOTE: ADD TG1 back in after uncommenting it above when we're ready for the feedback loop
        self.shooter.config_kP(kLoop, 3, kTimeout)
        self.shooter.config_kI(kLoop, 0, kTimeout)
        self.shooter.config_kD(kLoop, 0, kTimeout)

        # self.ourTimer = wpilib.Timer()

###NEW###- #request by shooter team to run contasntly counter-clockwise, and then run clockwise with the button push

        #code for the kicker component
        self.kicker = ctre.TalonSRX(10) #changed from 6 to 10
        self.kicker.setInverted(True) ##3/29fix: set to false- needeed to spin the other way
        self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

        #set mode to coast, meaning that the back-emf will not be generated (back electromotive force)
        self.kicker.setNeutralMode(ctre._ctre.NeutralMode.Coast)

        #set up variables equal to encoder positions
        self.kickerEncodePos = self.kicker.getSelectedSensorPosition()

        #code for the tread component
        self.tread = ctre.TalonSRX(8) #change from 7 to 8
        self.tread.setInverted(True)
        self.tread.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

        #set mode to coast, meaning that the back-emf will not be generated (back electromotive force)
        self.tread.setNeutralMode(ctre._ctre.NeutralMode.Coast)

        #set up variables equal to encoder positions
        self.treadEncodePos = self.tread.getSelectedSensorPosition()


        #code for the collector component
        self.collector = ctre.TalonSRX(7) #change from 8 to 7
        self.collector.setInverted(False)  
        self.collector.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
        #set mode to coast, meaning that the back-emf will not be generated (back electromotive force)
        self.kicker.setNeutralMode(ctre._ctre.NeutralMode.Coast)


        #set up joysticks
        self.l_joy = wpilib.Joystick(0)
        self.r_joy = wpilib.Joystick(1)


    # def autonomousInit(self):

    #     #restart timer
    #     self.ourTimer.reset()
    #     self.ourTimer.start()

    #     #set sensor position to 0
    #     self.l_motorFront.setSelectedSensorPosition(0)
    #     self.r_motorFront.setSelectedSensorPosition(0)
    #     self.shooter.setSelectedSensorPosition(0)

    #     '''
    #     self.kicker.setSelectedSensorPosition(0)
    #     self.tread.setSelectedSensorPosition(0)
    #     self.collector.setSelectedSensorPosition(0)
    #     '''

    #     #sets state at the begining for the dead reckoning
    #     self.autoState = 1
    #     self.plan = 1

    # def autonomousPeriodic(self):

    #     #update position variable every time periodic runs
    #     self.l_motorEncodePos = self.l_motorBack.getSelectedSensorPosition
    #     self.r_motorEncodePos = self.r_motorBack.getSelectedSensorPosition

    #     #update speed variable every time periodic runs
    #     self.l_motorEncodeSpeed = self.l_motorBack.getSelectedSensorPosition()
    #     self.r_motorEncodeSpeed = self.r_motorBack.getSelectedSensorPosition()


    #     #calls the function to calculate rotations to distance and sets it to new variable
    #     self.l_distance = self.encoderToInch(self.l_motorEncodePos)
    #     self.r_distance = self.encoderToInch(self.r_motorEncodePos)

    #     #set new variable to speed of motors
    #     l_vel = self.encoderSpeedInPerSec(self.l_motorEncodeSpeed)
    #     r_vel = self.encoderSpeedInPerSec(self.r_motorEncodeSpeed)


    #     wpilib.SmartDashboard.putString('DB/String 0', 'left inches/second:   {:5.3f}'.format(l_vel()))
    #     wpilib.SmartDashboard.putString('DB/String 1', 'right inches/second:   {:5.3f}'.format(r_vel()))
    #     wpilib.SmartDashboard.putString('DB/String 2', 'left position:   {:5.3f}'.format(self.l_distance()))
    #     wpilib.SmartDashboard.putString('DB/String 3', 'right position:   {:5.3f}'.format(self.r_distance()))


    #     #variable is equal to timer started in auto init
    #     Time = self.ourTimer.get()

    #     if self.autoState == 1:
    #         if self.plan == 1, 2, 3, 4, 5, 6:
    #             self.l_motorFront.set(-1.0)
    #             self.r_motorFront.set(-1.0)
    #         if Time >= 5:
    #             self.autostate = 2
    #     if self.autostate == 2:
    #         if self.plan == 1:
    #             self.l_motorFront.set()
    #         if self.plan == 2:
    #             self.l_motorFront.set()



    def disabledInit(self):

        #this function gets called once when the robot is disabled. in the past, we have not used this function, but it could occasionally be useful. in this case, we reset some SmartDashboard values
        wpilib.SmartDashboard.putString('DB/String 0',"")
        wpilib.SmartDashboard.putString('DB/String 1',"")
        wpilib.SmartDashboard.putString('DB/String 2',"")
        wpilib.SmartDashboard.putString('DB/String 3',"")
        wpilib.SmartDashboard.putString('DB/String 4',"")
        wpilib.SmartDashboard.putString('DB/String 5',"")
        wpilib.SmartDashboard.putString('DB/String 6',"")
        wpilib.SmartDashboard.putString('DB/String 7',"")
        wpilib.SmartDashboard.putString('DB/String 8',"")
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
        #  ====> VERY IMPORTANT FOR FIRST TEST
        self.l_motorFront.set(ctre._ctre.ControlMode.PercentOutput, left_command)
        self.r_motorFront.set(ctre._ctre.ControlMode.PercentOutput, right_command)

        # #alternate drive train code where we get Y from joystick
        # self.l_motorFront = self.left_command.getY()
        # self.r_motorFront = self.right_command.getY()

        #update position variable every time periodic runs
        self.l_motorEncodePos = self.l_motorBack.getSelectedSensorPosition()
        self.r_motorEncodePos = self.r_motorBack.getSelectedSensorPosition()

        #update speed variable every time periodic runs
        self.l_motorEncodeSpeed = self.l_motorBack.getSelectedSensorVelocity()
        self.r_motorEncodeSpeed = self.r_motorBack.getSelectedSensorVelocity()


        #calls the function to calculate rotations to distance and sets it to new variable
        self.l_distance = self.encoderToInch(self.l_motorEncodePos)
        self.r_distance = self.encoderToInch(self.r_motorEncodePos)

        #set new variable to speed of motors
        l_vel = self.encoderSpeedInPerSec(self.l_motorEncodeSpeed)
        r_vel = self.encoderSpeedInPerSec(self.r_motorEncodeSpeed)

        wpilib.SmartDashboard.putString('DB/String 0', 'left joystick:   {:5.3f}'.format(left_command))
        wpilib.SmartDashboard.putString('DB/String 1', 'right joystick: {:5.3f}'.format(right_command))
        wpilib.SmartDashboard.putString('DB/String 2', 'left inches/second:   {:5.3f}'.format(l_vel))
        wpilib.SmartDashboard.putString('DB/String 3', 'right inches/second:   {:5.3f}'.format(r_vel))
        wpilib.SmartDashboard.putString('DB/String 4', 'left position:   {:5.3f}'.format(self.l_distance))
        wpilib.SmartDashboard.putString('DB/String 5', 'right position:   {:5.3f}'.format(self.r_distance))



        # if self.l_joy.getRawButton(8):
        #     self.collector_piston.set(wpilib._wpilib.DoubleSolenoid.Value.kReverse)
        # elif self.l_joy.getRawButton(9):
        #     self.collector_piston.set(wpilib._wpilib.DoubleSolenoid.Value.kForward)


        self.shooterEncodePos = self.shooter.getSelectedSensorPosition()
        self.shooterSpeed = self.shooter.getSelectedSensorVelocity()


        #The following 10 lines of code do this: when button 2 is pushed, the collector and pulley (tread) will spin.  
        #   IF they're spinning, meaning button two is being held down, then the kicker can be turned on with button 4.
        #   If button 2 isn't pushed, do nothing, hence not allow button 4 and the kicker to be pushed.
        if self.l_joy.getRawButton(2):
            self.tread.set(ctre._ctre.ControlMode.PercentOutput, 0.25)
            self.collector.set(ctre._ctre.ControlMode.PercentOutput, 0.25)
            #set abovw two to 25% output, because it was too fast to be safe
            if self.l_joy.getRawButton(4):
                self.kicker.set(ctre._ctre.ControlMode.PercentOutput, -0.5)
            else:
                self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
        else:                                                                   #originally we thought we could get away without the "else," but it would just keep spinning
            self.collector.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
            self.tread.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

            
        ## this is for the collector and tread to go opposite direction- mght not need, but leave for now.
    #         if self.l_joy.getRawButton(4):
    #             self.collector.set(ctre._ctre.ControlMode.PercentOutput, -0.45)
    #             self.tread.set(ctre._ctre.ControlMode.PercentOutput, -0.45)
    #         else:
    #             self.collector.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
    #             self.tread.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
 
        if self.l_joy.getRawButton(1):
        ##3/29 FIX:  when 1 is pushed, the motor fights itself and jumps back and forth
            #self.shooter.set(ctre._ctre.ControlMode.PercentOutput, 0.75)
            self.shooter.set(ctre._ctre.ControlMode.Velocity, self.targetVelocity)
            if 11000 <= self.shooterSpeed and self.shooterSpeed <= 11050:
                if self.l_joy.getRawButton(1):
                    self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.75)
                    #self.Tread.set(ctre._ctre.ControlMode.PercentOutput, 0.55)
                else: ##NOTE: need to change this to always on reverse somewhere under new planning
                    self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
            else:
                self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
                # self.man1Tread.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
        else:
            self.shooter.set(ctre._ctre.ControlMode.PercentOutput, 0.0)
            self.kicker.set(ctre._ctre.ControlMode.PercentOutput, 0.0)

    def encoderToInch(self, encodeCounts):
        return encodeCounts / 2048 / 10.75 * 18.84

    def encoderSpeedInPerSec(self, unitsPerTenthSec):
        rotationsPerSec = unitsPerTenthSec * 10 / 2048
        distancePerSec = rotationsPerSec / 10.75 * 18.84
        return distancePerSec



if __name__ == "__main__":
    wpilib.run(MyRobot)