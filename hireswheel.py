#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-
# ------------------------------------------------------------------------------
# Python Test Box
# ------------------------------------------------------------------------------
""" @package    pyhid.hidpp.features.hireswheel

@brief  HID++ 2.0 HiResWheel command interface definition

@author Andy Su

@date   2019/3/19
"""
# ----------------------------------------------------------------------------
# imports
# ----------------------------------------------------------------------------

from pyhid.bitfield                  import BitField
from pyhid.hidpp.hidppmessage        import HidppMessage, TYPE
from pyhid.field                     import CheckByte
from pyhid.field                     import CheckHexList
from pyhid.field                     import CheckInt
from pylibrary.tools.hexlist         import HexList
from pylibrary.tools.numeral         import Numeral


# ----------------------------------------------------------------------------
# implementation
# ----------------------------------------------------------------------------


class HiResWheel(HidppMessage):
    """
    HiResWheel implementation class

    Format:
    || @b Name                || @b Bit count ||
    || ReportID               || 8            ||
    || DeviceIndex            || 8            ||
    || FeatureIndex           || 8            ||
    || FunctionID             || 4            ||
    || softwareID             || 4            ||
    || Params                 || 24           ||
    """
    FEATURE_ID = 0x2121
    MAX_FUNCTION_INDEX = 3

    def __init__(self, deviceIndex, featureIndex):
        """
        Constructor

        @param  deviceIndex            [in] (int)  Device Index
        @param  featureIndex           [in] (int)  feature Index
        """
        super(HiResWheel, self).__init__()

        self.deviceIndex = deviceIndex
        self.featureIndex = featureIndex
# end class HiResWheel


class GetWheelCapability(HiResWheel):
    """
    HiResWheel GetWheelCapability implementation class

    Returns the static capability information about the device.

    Format:
    || @b Name                || @b Bit count ||
    || ReportID               || 8            ||
    || DeviceIndex            || 8            ||
    || FeatureIndex           || 8            ||
    || FunctionID             || 4            ||
    || SoftwareID             || 4            ||
    || Padding                || 24           ||
    """

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        PADDING = 0xFA

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        PADDING = 0x18

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId):
        """
        Constructor

        @param  deviceIndex            [in] (int)  Device Index
        @param  featureId              [in] (int)  desired feature Id
        """
        super(GetWheelCapability, self).__init__(deviceIndex, featureId)

        self.functionIndex = GetWheelCapabilityResponse.FUNCTION_INDEX
    # end def __init__
# end class GetWheelCapability


class GetWheelCapabilityResponse(HiResWheel):
    """
    HiResWheel GetWheelCapability response implementation class

    Returns the static capability information about the device.

    Format:
    || @b Name          || @b Bit count ||
    || ReportID         || 8            ||
    || DeviceIndex      || 8            ||
    || FeatureIndex     || 8            ||
    || FunctionID       || 4            ||
    || SoftwareID       || 4            ||
    || Multiplier       || 8            ||
    || Capabilities     || 8            ||
    || Padding          || 112          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    REQUEST_LIST = (GetWheelCapability)
    FUNCTION_INDEX = 0
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        MULTIPLIER    = 0xFA
        CAPABILITIES  = 0xF9
        PADDING       = 0xF8

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        MULTIPLIER    = 0x08
        CAPABILITIES  = 0x08
        PADDING       = 0x70

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.MULTIPLIER,
                 LEN.MULTIPLIER,
                 0x00,
                 0x00,
                 title='Multiplier',
                 name='multiplier',
                 checks=(CheckHexList(LEN.MULTIPLIER // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.CAPABILITIES,
                 LEN.CAPABILITIES,
                 0x00,
                 0x00,
                 title='Capabilities',
                 name='capabilities',
                 checks=(CheckHexList(LEN.CAPABILITIES // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId,
                        multiplier,
                        capabilities):
        """
        Constructor

        @param  deviceIndex      [in] (int)  Device Index
        @param  featureId        [in] (int)  desired feature Id
        @param  multiplier       [in] (int)  returned multiplier
        @param  capabilities     [in] (int)  returned capabilities
        """
        super(GetWheelCapabilityResponse, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.multiplier = multiplier
        self.capabilities = capabilities
    # end def __init__
# end class GetWheelCapabilityResponse


class GetWheelMode(HiResWheel):
    """
    HiResWheel GetWheelMode implementation class

    Returns the current wheel mode about the device.

    Format:
    || @b Name                || @b Bit count ||
    || ReportID               || 8            ||
    || DeviceIndex            || 8            ||
    || FeatureIndex           || 8            ||
    || FunctionID             || 4            ||
    || SoftwareID             || 4            ||
    || Padding                || 24           ||
    """

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        PADDING = 0xFA

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        PADDING = 0x18

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId):
        """
        Constructor

        @param  deviceIndex            [in] (int)  Device Index
        @param  featureId              [in] (int)  desired feature Id
        """
        super(GetWheelMode, self).__init__(deviceIndex, featureId)

        self.functionIndex = GetWheelModeResponse.FUNCTION_INDEX
    # end def __init__
# end class GetWheelMode


class GetWheelModeResponse(HiResWheel):
    """
    HiResWheel GetWheelMode response implementation class

    Returns the current wheel mode about the device.

    Format:
    || @b Name               || @b Bit count ||
    || ReportID              || 8            ||
    || DeviceIndex           || 8            ||
    || FeatureIndex          || 8            ||
    || FunctionID            || 4            ||
    || SoftwareID            || 4            ||
    || WheelMode             || 8            ||
    || Padding               || 120          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    REQUEST_LIST = (GetWheelMode)
    FUNCTION_INDEX = 1
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        WHEEL_MODE   = 0xFA
        PADDING      = 0xF9

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        WHEEL_MODE   = 0x08
        PADDING      = 0x78

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.WHEEL_MODE,
                 LEN.WHEEL_MODE,
                 0x00,
                 0x00,
                 title='Wheel Mode',
                 name='wheelMode',
                 checks=(CheckHexList(LEN.WHEEL_MODE // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId,
                        wheelMode):
        """
        Constructor

        @param  deviceIndex          [in] (int)      Device Index
        @param  featureId            [in] (int)      desired feature Id
        @param  wheelMode            [in] (int)      returned mode of wheel
        """
        super(GetWheelModeResponse, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.wheelMode = wheelMode
    # end def __init__
# end class GetWheelModeResponse


class SetWheelMode(HiResWheel):
    """
    HiResWheel SetWheelMode implementation class

    Returns the setting wheel mode about the device.

    Format:
    || @b Name                || @b Bit count ||
    || ReportID               || 8            ||
    || DeviceIndex            || 8            ||
    || FeatureIndex           || 8            ||
    || FunctionID             || 4            ||
    || SoftwareID             || 4            ||
    || WheelMode              || 8            ||
    || Padding                || 16           ||
    """

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        WHEEL_MODE = 0xFA
        PADDING    = 0xF9

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        WHEEL_MODE = 0x08
        PADDING    = 0x10

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.WHEEL_MODE,
                 LEN.WHEEL_MODE,
                 0x00,
                 0x00,
                 title='Wheel Mode',
                 name='wheelMode',
                 checks=(CheckHexList(LEN.WHEEL_MODE // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),
        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId,
                        wheelMode):
        """
        Constructor

        @param  deviceIndex            [in] (int)  Device Index
        @param  featureId              [in] (int)  desired feature Id
        @param  wheelMode              [in] (int)  mode of wheel
        """
        super(SetWheelMode, self).__init__(deviceIndex, featureId)

        self.functionIndex = SetWheelModeResponse.FUNCTION_INDEX
        self.wheelMode = wheelMode
    # end def __init__
# end class SetWheelMode


class SetWheelModeResponse(HiResWheel):
    """
    HiResWheel SetWheelMode response implementation class

    Returns the setting wheel mode about the device.

    Format:
    || @b Name               || @b Bit count ||
    || ReportID              || 8            ||
    || DeviceIndex           || 8            ||
    || FeatureIndex          || 8            ||
    || FunctionID            || 4            ||
    || SoftwareID            || 4            ||
    || WheelMode             || 8            ||
    || Padding               || 120          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    REQUEST_LIST = (SetWheelMode)
    FUNCTION_INDEX = 2
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        WHEEL_MODE   = 0xFA
        PADDING      = 0xF9

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        WHEEL_MODE   = 0x08
        PADDING      = 0x78

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.WHEEL_MODE,
                 LEN.WHEEL_MODE,
                 0x00,
                 0x00,
                 title='Wheel Mode',
                 name='wheelMode',
                 checks=(CheckHexList(LEN.WHEEL_MODE // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId,
                        wheelMode):
        """
        Constructor

        @param  deviceIndex          [in] (int)      Device Index
        @param  featureId            [in] (int)      desired feature Id
        @param  wheelmode            [in] (int)      returned mode of wheel
        """
        super(SetWheelModeResponse, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.wheelMode = wheelMode
    # end def __init__
# end class SetWheelModeResponse


class GetRatchetSwitchState(HiResWheel):
    """
    HiResWheel GetRatchetSwitchState implementation class

    Returns the ratchet state about the device.

    Format:
    || @b Name                || @b Bit count ||
    || ReportID               || 8            ||
    || DeviceIndex            || 8            ||
    || FeatureIndex           || 8            ||
    || FunctionID             || 4            ||
    || SoftwareID             || 4            ||
    || Padding                || 24           ||
    """

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        PADDING = 0xFA

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        PADDING = 0x18

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId):
        """
        Constructor

        @param  deviceIndex            [in] (int)  Device Index
        @param  featureId              [in] (int)  desired feature Id
        """
        super(GetRatchetSwitchState, self).__init__(deviceIndex, featureId)

        self.functionIndex = GetRatchetSwitchStateResponse.FUNCTION_INDEX
    # end def __init__
# end class GetRatchetSwitchState


class GetRatchetSwitchStateResponse(HiResWheel):
    """
    HiResWheel GetRatchetSwitchState implementation class

    Returns the ratchet state about the device.

    Format:
    || @b Name          || @b Bit count ||
    || ReportID         || 8            ||
    || DeviceIndex      || 8            ||
    || FeatureIndex     || 8            ||
    || FunctionID       || 4            ||
    || SoftwareID       || 4            ||
    || RatchetMode      || 8            ||
    || Padding          || 120          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    REQUEST_LIST = (GetRatchetSwitchState)
    FUNCTION_INDEX = 3
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        RATCHET_MODE  = 0xFA
        PADDING       = 0xF9

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        RATCHET_MODE  = 0x08
        PADDING       = 0x78

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.RATCHET_MODE,
                 LEN.RATCHET_MODE,
                 0x00,
                 0x00,
                 title='Ratchet Mode',
                 name='ratchetMode',
                 checks=(CheckHexList(LEN.RATCHET_MODE // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                        featureId,
                        ratchetMode):
        """
        Constructor

        @param  deviceIndex      [in] (int)  Device Index
        @param  featureId        [in] (int)  desired feature Id
        @param  ratchetMode      [in] (int)  returned mode of ratchet
        """
        super(GetRatchetSwitchStateResponse, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.ratchetMode = ratchetMode
    # end def __init__
# end class GetRatchetSwitchStateResponse


class WheelMovement(HiResWheel):
    """
    HiResWheel WheelMovement implementation class

    Reported when "target" bit is set to 1 (HID++ notification).

    Format:
    || @b Name                    || @b Bit count ||
    || ReportID                   || 8            ||
    || DeviceIndex                || 8            ||
    || FeatureIndex               || 8            ||
    || FunctionID                 || 4            ||
    || SoftwareID                 || 4            ||
    || Resolution & Periods       || 8            ||
    || DeltaV                     || 16           ||
    || Padding                    || 104          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        RES_AND_PERIODS = 0xFA
        DELTA_V         = 0xF9
        PADDING         = 0xF8

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        RES_AND_PERIODS = 0x08
        DELTA_V         = 0x10
        PADDING         = 0x68

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.RES_AND_PERIODS,
                 LEN.RES_AND_PERIODS,
                 0x00,
                 0x00,
                 title='Resolution & Periods',
                 name='resAndPeriods',
                 checks=(CheckHexList(LEN.RES_AND_PERIODS // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.DELTA_V,
                 LEN.DELTA_V,
                 0x00,
                 0x00,
                 title='DeltaV',
                 name='deltaV',
                 checks=(CheckHexList(LEN.DELTA_V // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                 featureId,
                 resAndPeriods,
                 deltaV):
        """
        Constructor

        @param  deviceIndex           [in] (int)  Device Index
        @param  featureId             [in] (int)  desired feature Id
        @param  resAndPeriods         [in] (int)  returned resolution and periods
        @param  deltaV                [in] (int)  returned the vertical wheel motion delta
        """
        super(WheelMovement, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.resAndPeriods = resAndPeriods
        self.deltaV = deltaV
    # end def __init__
# end class WheelMovement


class RatchetSwitch(GetRatchetSwitchStateResponse):
    """
    HiResWheel RatchetSwitch implementation class

    Reported when ratchet switch state changes.

    Format:
    || @b Name                    || @b Bit count ||
    || ReportID                   || 8            ||
    || DeviceIndex                || 8            ||
    || FeatureIndex               || 8            ||
    || FunctionID                 || 4            ||
    || SoftwareID                 || 4            ||
    || RatchetMode                || 8            ||
    || Padding                    || 120          ||
    """
    MSG_TYPE = TYPE.RESPONSE
    VERSION = 0

    class FID(HiResWheel.FID):
        """
        Field Identifiers
        """
        RATCHET_MODE   = 0xFA
        PADDING        = 0xF9

    # end class FID

    class LEN(HiResWheel.LEN):
        """
        Field Lengths
        """
        RATCHET_MODE   = 0x08
        PADDING        = 0x78

    # end class LEN

    FIELDS = HiResWheel.FIELDS + (
        BitField(FID.RATCHET_MODE,
                 LEN.RATCHET_MODE,
                 0x00,
                 0x00,
                 title='Ratchet Mode',
                 name='ratchetMode',
                 checks=(CheckHexList(LEN.RATCHET_MODE // 8),
                         CheckByte(),),
                 conversions={HexList: Numeral}, ),

        BitField(FID.PADDING,
                 LEN.PADDING,
                 0x00,
                 0x00,
                 title='Padding',
                 name='padding',
                 checks=(CheckHexList(LEN.PADDING // 8),
                         CheckByte(),),
                 defaultValue=HiResWheel.DEFAULT.PADDING),
    )

    def __init__(self, deviceIndex,
                 featureId,
                 ratchetMode):
        """
        Constructor

        @param  deviceIndex           [in] (int)  Device Index
        @param  featureId             [in] (int)  desired feature Id
        @param  ratchetMode           [in] (int)  returned the mode of ratchet
        """
        super(RatchetSwitch, self).__init__(deviceIndex, featureId)

        self.functionIndex = self.FUNCTION_INDEX
        self.ratchetMode = ratchetMode
    # end def __init__
# end class RatchetSwitch


# ----------------------------------------------------------------------------
# END OF FILE
# ----------------------------------------------------------------------------