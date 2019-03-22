#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# ----------------------------------------------------------------------------
# Python Test Box
# ----------------------------------------------------------------------------
""" @package pytestbox.hid.mouse.feature_2121

@brief  Validates HID mouse feature 0x2121

@author Andy Su

@date   2019/3/19
"""
# ----------------------------------------------------------------------------
# imports
# ----------------------------------------------------------------------------
from pytestbox.base.basetest                        import BaseTestCase
from pyharness.selector                             import features
from pyharness.extensions                           import level
from pyhid.hidpp.features.error                     import ErrorCodes
from pylibrary.tools.hexlist                        import HexList
from pylibrary.tools.numeral                        import Numeral
from pylibrary.tools.util                           import computeSupValues
from pylibrary.tools.util                           import computeWrongRange
from pyhid.hidpp.features.hireswheel                import HiResWheel
from pyhid.hidpp.features.hireswheel                import GetWheelCapability
from pyhid.hidpp.features.hireswheel                import GetWheelCapabilityResponse
from pyhid.hidpp.features.hireswheel                import GetWheelMode
from pyhid.hidpp.features.hireswheel                import GetWheelModeResponse
from pyhid.hidpp.features.hireswheel                import SetWheelMode
from pyhid.hidpp.features.hireswheel                import SetWheelModeResponse
from pyhid.hidpp.features.hireswheel                import GetRatchetSwitchState
from pyhid.hidpp.features.hireswheel                import GetRatchetSwitchStateResponse

import unittest

# ----------------------------------------------------------------------------
# implementation
# ----------------------------------------------------------------------------

class HiResWheelTestCase(BaseTestCase):
    '''
    Validates HiRes Wheel TestCases
    '''

    def setUp(self):
        """
        Handles test prerequisites.
        """
        super(HiResWheelTestCase, self).setUp()

        # ---------------------------------------------------------------------------
        self.logTitle2('Prerequisite 1: Send Root.GetFeature(0x2121)')
        # ---------------------------------------------------------------------------
        self.featureId = self.updateFeatureMapping(featureId=HiResWheel.FEATURE_ID)

        # Function that analyze the response
        self.getUsefulBit = lambda desiredValue,desiredBit : bin(int(desiredValue))[2:].zfill(8)[desiredBit]
    # end def setUp

    @features('Feature2121')
    @level('Interface')
    def test_GetWheelCapability(self):
        """
        Validates GetWheelCapability normal processing (Feature 0x2121)

        HiRes Wheel
         multiplier, hasSwitch, hasInvert [0]GetWheelCapability
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send HiResWheel.GetWheelCapability')
        # ---------------------------------------------------------------------------
        getWheelCapability = GetWheelCapability(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId)
        self.device.sendReport(data=getWheelCapability)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=GetWheelCapabilityResponse)
        self.logTrace('GetWheelCapability Response: %s\n' % str(response))
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate GetWheelCapability.multiplier value')
        # ---------------------------------------------------------------------------
        f = self.getFeatures()
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Multiplier,
                         obtained=int(response.multiplier),
                         msg='The multiplier parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Validate GetWheelCapability.hasSwitch value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_HasSwitch,
                         obtained=getUsefulBit(response.capabilities, 2),
                         msg='The hasSwitch parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 3: Validate GetWheelCapability.hasInvert value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_HasInvert,
                         obtained=getUsefulBit(response.capabilities, 3),
                         msg='The hasInvert parameter differs from the one expected')

        self.testCaseChecked("FNT_2121_0001")
    # end def test_GetWheelCapability

    @features('Feature2121')
    @level('Interface')
    def test_GetWheelMode(self):
        """
        Validates GetWheelMode normal processing (Feature 0x2121)

        HiRes Wheel
         target, resolution, invert [1]GetWheelMode
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send HiResWheel.GetWheelMode')
        # ---------------------------------------------------------------------------
        getWheelMode = GetWheelMode(
           deviceIndex=self.deviceIndex,
            featureId=self.featureId)
        self.device.sendReport(data=getWheelMode)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=GetWheelModeResponse)
        self.logTrace('GetWheelMode Response: %s\n' % str(response))
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate GetWheelMode.target value')
        # ---------------------------------------------------------------------------
        f = self.getFeatures()
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Target_Default,
                         obtained=getUsefulBit(response.wheelMode, 0),
                         msg='The target parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Validate GetWheelMode.resolution value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Resolution_Default,
                         obtained=getUsefulBit(response.wheelMode, 1),
                         msg='The resolution parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 3: Validate GetWheelMode.invert value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Invert_Default,
                         obtained=getUsefulBit(response.wheelMode, 2),
                         msg='The invert parameter differs from the one expected')

        self.testCaseChecked("FNT_2121_0002")
    # end def test_GetWheelMode

    @features('Feature2121')
    @level('Interface')
    def test_SetWheelMode(self):
        """
        Validates SetWheelMode normal processing (Feature 0x2121)

        HiRes Wheel
         target, resolution, invert [2]SetWheelMode(target, resolution, invert)
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send SetWheelMode with parameter value (1,1,1)')
        # ---------------------------------------------------------------------------
        setWheelMode = SetWheelMode(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId,
            wheelMode=7)
        self.device.sendReport(data=setWheelMode)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=SetWheelModeResponse)
        self.logTrace('SetWheelMode Response: %s\n' % str(response))
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate SetWheelMode.target value')
        # ---------------------------------------------------------------------------
        f = self.getFeatures()
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Target,
                         obtained=getUsefulBit(response.wheelMode, 0),
                         msg='The target parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Validate SetWheelMode.resolution value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Resolution,
                         obtained=getUsefulBit(response.wheelMode, 1),
                         msg='The resolution parameter differs from the one expected')
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 3: Validate SetWheelMode.invert value')
        # ---------------------------------------------------------------------------
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Invert,
                         obtained=getUsefulBit(response.wheelMode, 2),
                         msg='The invert parameter differs from the one expected')

        # Reset the parameters for other tests
        setWheelMode = SetWheelMode(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId,
            wheelMode=0)
        self.device.sendReport(data=setWheelMode)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=SetWheelModeResponse)
        self.logTrace('SetWheelMode Response: %s\n' % str(response))

        self.testCaseChecked("FNT_2121_0003")
    # end def test_SetWheelMode

    @features('Feature2121')
    @level('Business')
    def test_SetWheelModeWithAllSets(self):
        """
        Validates SetWheelMode Business case sequence (Feature 0x2121)

        HiRes Wheel
         target, resolution, invert [1]GetWheelMode
         target, resolution, invert [2]SetWheelMode(target, resolution, invert)
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send SetWheelMode with the 3 bits set consist of (0,1) for each bit')
        # ---------------------------------------------------------------------------
        for modeValue in range(0, 8):
            setWheelMode = SetWheelMode(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId,
                wheelMode=modeValue)
            self.device.sendReport(data=setWheelMode)
            responseFromSet = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                       classType=SetWheelModeResponse)
            self.logTrace('SetWheelMode Response: %s\n' % str(responseFromSet))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Step 2: Test Step 2: Send HiResWheel.GetWheelMode')
            # ---------------------------------------------------------------------------
            getWheelMode = GetWheelMode(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId)
            self.device.sendReport(data=getWheelMode)
            responseFromGet = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                              classType=GetWheelModeResponse)
            self.logTrace('SetWheelMode Response: %s\n' % str(responseFromGet))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 1: Compare return value of SetWheelMode.target with GetWheelMode.target ')
            # ---------------------------------------------------------------------------
            f = self.getFeatures()
            self.assertEqual(expected=getUsefulBit(responseFromSet.wheelMode, 0),
                             obtained=getUsefulBit(responseFromGet.wheelMode, 0),
                             msg='The target parameter differs from the one expected')
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 2: Compare return value of SetWheelMode.resolution with GetWheelMode.resolution')
            # ---------------------------------------------------------------------------
            self.assertEqual(expected=getUsefulBit(responseFromSet.wheelMode, 1),
                             obtained=getUsefulBit(responseFromSet.wheelMode, 1),
                             msg='The resolution parameter differs from the one expected')
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 3: Compare return value of SetWheelMode.invert with GetWheelMode.invert ')
            # ---------------------------------------------------------------------------
            self.assertEqual(expected=getUsefulBit(responseFromSet.wheelMode, 2),
                             obtained=getUsefulBit(responseFromSet.wheelMode, 2),
                             msg='The invert parameter differs from the one expected')
        # end for

        # Reset the parameters for other tests
        setWheelMode = SetWheelMode(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId,
            wheelMode=0)
        self.device.sendReport(data=setWheelMode)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=SetWheelModeResponse)
        self.logTrace('SetWheelMode Response: %s\n' % str(response))

        self.testCaseChecked("FNT_2121_0004")
    # end def test_SetWheelModeWithAllSets

    @features('Feature2121')
    @level('Interface')
    def test_GetRatchetSwitchState(self):
        """
        Validate GetRatchetSwitchState normal processing (Feature 0x2121)

        HiRes Wheel
         state [3]GetRatchetSwitchState
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send GetRatchetSwitchState')
        # ---------------------------------------------------------------------------
        getRatchetSwitchState = GetRatchetSwitchState(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId)
        self.device.sendReport(data=getRatchetSwitchState)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=GetRatchetSwitchStateResponse)
        self.logTrace('GetRatchetSwitchState Response: %s\n' % str(response))
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate GetRatchetSwitchState.state value')
        # ---------------------------------------------------------------------------
        f = self.getFeatures()
        self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_RatchetMode,
                         obtained=getUsefulBit(response.ratchetMode, 0),
                         msg='The ratchetMode parameter differs from the one expected')

        self.testCaseChecked("FNT_2121_0005")
    # end def test_GetRatchetSwitchState

    @unittest.skip("Need external robust arm to press the button")
    @features('Feature2121')
    @level('Interface')
    def test_RatchetSwitch(self):
        """
        Validate RatchetSwitch normal processing (Feature 0x2121)

        HiRes Wheel
         state [event1]RatchetSwitch
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Press the free-spin button to change the ratchet mode')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate the return value of RatchetSwitch.state')
        # ---------------------------------------------------------------------------

        self.testCaseChecked("FNT_2121_0006")
    # end def test_RatchetSwitch

    @unittest.skip("Need external robust arm to press the button")
    @features('Feature2121')
    @level('Business')
    def test_RatchetSwitchWithTwoPress(self):
        """
        Validate RatchetSwitch Business case sequence (Feature 0x2121)

        HiRes Wheel
         state [event1]RatchetSwitch
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Press the free-spin button to change the ratchet mode')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Compare the return value of RatchetSwitch.state with GetRatchetSwitchState.state')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 2: Press the free-spin button to change the ratchet mode again')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Compare the return value of RatchetSwitch.state with GetRatchetSwitchState.state')
        # ---------------------------------------------------------------------------

        self.testCaseChecked("FNT_2121_0007")
    # end def test_RatchetSwitchWithTwoPress

    @unittest.skip("Need external robust arm to roll the wheel")
    @features('Feature2121')
    @level('Interface')
    def test_WheelMovement(self):
        """
        Validate WheelMovement normal processing (Feature 0x2121)

        HiRes Wheel
         resolution, periods, deltaV [event0]WheelMovement
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Roll the mouse wheel')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate WheelMovement.resolution value')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Validate WheelMovement.periods value')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 3: Validate WheelMovement.deltaV value')
        # ---------------------------------------------------------------------------

        self.testCaseChecked("FNT_2121_0008")
    # end def test_WheelMovement

    @unittest.skip("Need external robust arm to roll the wheel")
    @features('Feature2121')
    @level('Business')
    def test_WheelMovementRollUpAndDown(self):
        """
        Validate WheelMovement Business case sequence (Feature 0x2121)

        HiRes Wheel
         resolution, periods, deltaV [event0]WheelMovement
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send SetWheelMode with the 3 bits set consist of (0,1) for each bit')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 2: Send GetWheelMode')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 3: Spin up and spin down the wheel')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Compare the return value of GetWheelMode.resolution with WheelMovement.resolution')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 2: Validate WheelMovement.periods value')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 3: Validate change of WheelMovement.deltaV according to the GetWheelMode.resolution '
                       'and GetWheelMode.invert')
        # ---------------------------------------------------------------------------

        self.testCaseChecked("FNT_2121_0009")
    # end def test_WheelMovement

    @unittest.skip("Need external robust arm to roll the wheel")
    @features('Feature2121')
    @level('Functionality')
    def test_WheelMovementPeriodValue(self):
        """
        Validate if WheelMovement.period is not equal to 1 when interrupt by changing
        rachet mode or send SetWheelMode (Feature 0x2121)

        HiRes Wheel
         resolution, periods, deltaV [event0]WheelMovement
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Scroll up and down the wheel')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 2: Press the free-spin button to change the ratchet mode')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 3: Send SetWheelMode')
        # ---------------------------------------------------------------------------

        # ---------------------------------------------------------------------------
        self.logTitle2('Test Check 1: Validate if WheelMovement.periods change to 2 after the interrupt event')
        # ---------------------------------------------------------------------------

        self.testCaseChecked("FNT_2121_0010")
    # end def test_WheelMovementPeriodValue

    @features('Feature2121')
    @level('ErrorHandling')
    def test_WrongFunctionIndex(self):
        """
        Validates HiResWheel robustness processing

        Function indexes valid range [0..3],
            Tests wrong indexes
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send GetWheelCapability with wrong index value')
        # ---------------------------------------------------------------------------
        for functionIndex in computeWrongRange([x for x in range(HiResWheel.MAX_FUNCTION_INDEX + 1)],
                                               maxValue=0xF):
            getWheelCapability = GetWheelCapability(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId)
            getWheelCapability.functionIndex = int(functionIndex)
            self.device.sendReport(data=getWheelCapability)
            response = self.getMessage(queue=self.hidDispatcher.errorMessageQueue,
                                       classType=ErrorCodes)
            self.logTrace('GetWheelCapability Error Response: %s\n' % str(response))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 1: Check Error Codes InvalidFunctionId (7)  returned by the device')
            # ---------------------------------------------------------------------------
            self.assertEqual(expected=getWheelCapability.featureIndex,
                             obtained=response.featureIndex,
                             msg='The request and response feature indexes differ !')
            self.assertEqual(expected=ErrorCodes.INVALID_FUNCTION_ID,
                             obtained=response.errorCode,
                             msg='The received error code do not match the expected one !')
        # end for

        self.testCaseChecked("ROT_1000_0001")
    # end def test_WrongIndex

    @features('Feature2121')
    @level('Robustness')
    def test_OtherRsvBits(self):
        """
        Validate SetWheelMode Only care about last 3 bits

        wheelMode = [2]SetWheelMode(target, resolution, invert)
        Request: 0x10.DeviceIndex.FeatureIndex.0x0F.0xFF.0x00.0x00
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send SetWheelMode with several value for wheelMode')
        # ---------------------------------------------------------------------------
        for powerValue in range(3, 8):
            modeValue = 3 + pow(2, powerValue)
            setWheelMode = SetWheelMode(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId,
                wheelMode=modeValue)
            self.device.sendReport(data=setWheelMode)
            response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                       classType=SetWheelModeResponse)
            self.logTrace('SetWheelMode Response: %s\n' % str(response))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 1: Validate SetWheelMode response received')
            # ---------------------------------------------------------------------------
            f = self.getFeatures()
            self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Target,
                             obtained=int(getUsefulBit(response.wheelMode, 1)),
                             msg='The target parameter differs from the one expected')
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 2: Validate if reservation bits of output is same as input')
            # ---------------------------------------------------------------------------
            self.assertEqual(expected=modeValue,
                             obtained=int(response.wheelMode),
                             msg='The target parameter differs from the one expected')

        # end for

        # Reset the parameters for other tests
        setWheelMode = SetWheelMode(
            deviceIndex=self.deviceIndex,
            featureId=self.featureId,
            wheelMode=0)
        self.device.sendReport(data=setWheelMode)
        response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                   classType=SetWheelModeResponse)
        self.logTrace('SetWheelMode Response: %s\n' % str(response))

        self.testCaseChecked("ROT_1000_0002")
    # end def test_WrongIndex

    @features('Feature2121')
    @level('Robustness')
    def test_OtherSoftwareId(self):
        """
        Validates HiResWheel softwareId are ignored

        getWheelCapability = [0]GetWheelCapability
        Request: 0x10.DeviceIndex.FeatureIndex.0x00.0x00.0x00.0x00
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send GetWheelCapability with several value for softwareId')
        # ---------------------------------------------------------------------------
        for softwareId in range(1, 0x10):
            getWheelCapability = GetWheelCapability(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId)
            getWheelCapability.softwareId = softwareId
            self.device.sendReport(data=getWheelCapability)
            response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                       classType=GetWheelCapabilityResponse)
            self.logTrace('GetWheelCapability Response: %s\n' % str(response))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 1: Validate GetWheelCapability response received')
            # ---------------------------------------------------------------------------
            f = self.getFeatures()
            self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Multiplier,
                             obtained=int(response.multiplier),
                             msg='The multiplier parameter differs from the one expected')
        # end for

        self.testCaseChecked("ROT_2201_0003")
    # end def test_OtherSoftwareId

    @features('Feature2121')
    @level('Robustness')
    def test_OtherPaddingBytes(self):
        """
        Validates HiResWheel softwareId are ignored

        getWheelCapability = [0]GetWheelCapability
        Request: 0x10.DeviceIndex.FeatureIndex.0x0F.0xAA.0xBB.0xCC
        """
        # ---------------------------------------------------------------------------
        self.logTitle2('Test Step 1: Send GetWheelCapability with several value for padding')
        # ---------------------------------------------------------------------------
        for paddingByte in computeSupValues(HexList(Numeral(GetWheelCapability.DEFAULT.PADDING,
                                                            GetWheelCapability.LEN.PADDING // 8))):
            getWheelCapability = GetWheelCapability(
                deviceIndex=self.deviceIndex,
                featureId=self.featureId)
            getWheelCapability.padding = paddingByte
            self.device.sendReport(data=getWheelCapability)
            response = self.getMessage(queue=self.hidDispatcher.mouseMessageQueue,
                                       classType=GetWheelCapabilityResponse)
            self.logTrace('GetWheelCapabilityResponse: %s\n' % str(response))
            # ---------------------------------------------------------------------------
            self.logTitle2('Test Check 1: Validate GetWheelCapability response received')
            # ---------------------------------------------------------------------------
            f = self.getFeatures()
            self.assertEqual(expected=f.PRODUCT.MOUSE.HIRESWHEEL.F_Multiplier,
                             obtained=int(response.multiplier),
                             msg='The multiplier parameter differs from the one expected')
        # end for

        self.testCaseChecked("ROT_2201_0004")
    # end def test_OtherPaddingBytes

# end class HiResWheelTestCase

# Function that analyze the response and get the bit you want
def getUsefulBit(desiredValue, desiredBit):
    return int(bin(int(desiredValue))[2:].zfill(8)[::-1][desiredBit])

# ----------------------------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------------------------
