# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 12:02:05 2019

@author: agonzal2
"""

<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>Dialog</class>
 <widget class="QDialog" name="Dialog">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>493</width>
    <height>674</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>Ephys</string>
  </property>
  <widget class="QLabel" name="label">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>180</y>
     <width>321</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Epochs</string>
   </property>
  </widget>
  <widget class="QFrame" name="frameEpochs">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>200</y>
     <width>471</width>
     <height>91</height>
    </rect>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QPushButton" name="ButtonGetEpochs">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>10</y>
      <width>211</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Get Epochs from Excel file</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ButtonPlotEpochs">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>10</y>
      <width>141</width>
      <height>21</height>
     </rect>
    </property>
    <property name="text">
     <string>Plot Epochs</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ButtonPlotEpochsAverage">
    <property name="geometry">
     <rect>
      <x>290</x>
      <y>60</y>
      <width>141</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Plot Epochs Average</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_11">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>40</y>
      <width>59</width>
      <height>15</height>
     </rect>
    </property>
    <property name="text">
     <string>tmax(s)</string>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="doubleSpinBoxTmax">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>60</y>
      <width>66</width>
      <height>24</height>
     </rect>
    </property>
    <property name="decimals">
     <number>3</number>
    </property>
    <property name="minimum">
     <double>-2.000000000000000</double>
    </property>
    <property name="maximum">
     <double>4.000000000000000</double>
    </property>
    <property name="singleStep">
     <double>0.100000000000000</double>
    </property>
    <property name="value">
     <double>4.000000000000000</double>
    </property>
   </widget>
   <widget class="QLabel" name="label_12">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>40</y>
      <width>59</width>
      <height>15</height>
     </rect>
    </property>
    <property name="text">
     <string>tmin(s)</string>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="doubleSpinBoxTmin">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>60</y>
      <width>66</width>
      <height>24</height>
     </rect>
    </property>
    <property name="decimals">
     <number>3</number>
    </property>
    <property name="minimum">
     <double>-2.000000000000000</double>
    </property>
    <property name="maximum">
     <double>4.000000000000000</double>
    </property>
    <property name="singleStep">
     <double>0.100000000000000</double>
    </property>
    <property name="value">
     <double>-2.000000000000000</double>
    </property>
   </widget>
  </widget>
  <widget class="QFrame" name="frame_2">
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>50</y>
     <width>321</width>
     <height>111</height>
    </rect>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QPushButton" name="ButtonPlotRawData">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>20</y>
      <width>131</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Plot Raw Data</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ButtonLoadData">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>40</y>
      <width>101</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Load Raw Data</string>
    </property>
   </widget>
   <widget class="QPushButton" name="ButtonFilterRawData">
    <property name="enabled">
     <bool>false</bool>
    </property>
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>60</y>
      <width>131</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Filter Raw Data</string>
    </property>
   </widget>
  </widget>
  <widget class="QLabel" name="label_2">
   <property name="geometry">
    <rect>
     <x>60</x>
     <y>30</y>
     <width>101</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Raw Data</string>
   </property>
  </widget>
  <widget class="QFrame" name="framePlottingEvoked">
   <property name="enabled">
    <bool>false</bool>
   </property>
   <property name="geometry">
    <rect>
     <x>10</x>
     <y>300</y>
     <width>471</width>
     <height>361</height>
    </rect>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
   <widget class="QPushButton" name="ButtonPlotSingleTopomap">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>20</y>
      <width>191</width>
      <height>25</height>
     </rect>
    </property>
    <property name="text">
     <string>Plot Single Topomap</string>
    </property>
   </widget>
   <widget class="QSlider" name="SliderSingleTopomap">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>60</y>
      <width>281</width>
      <height>16</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QSlider" name="SliderFinalTopomap">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>160</y>
      <width>281</width>
      <height>16</height>
     </rect>
    </property>
    <property name="maximum">
     <number>99</number>
    </property>
    <property name="value">
     <number>0</number>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QSlider" name="SliderInitialTopomap">
    <property name="geometry">
     <rect>
      <x>120</x>
      <y>130</y>
      <width>281</width>
      <height>16</height>
     </rect>
    </property>
    <property name="orientation">
     <enum>Qt::Horizontal</enum>
    </property>
   </widget>
   <widget class="QPushButton" name="ButtonPlotTopomapBetweenEvoked">
    <property name="geometry">
     <rect>
      <x>160</x>
      <y>100</y>
      <width>191</width>
      <height>23</height>
     </rect>
    </property>
    <property name="text">
     <string>Plot Topomap between Evoked</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_3">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>60</y>
      <width>121</width>
      <height>20</height>
     </rect>
    </property>
    <property name="text">
     <string>Evoked number</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>130</y>
      <width>111</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Initial Evoked</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_5">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>160</y>
      <width>101</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Final Evoked</string>
    </property>
   </widget>
   <widget class="QSpinBox" name="spinBoxInitialTopomap">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>120</y>
      <width>47</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QSpinBox" name="spinBoxSingleTopomap">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>50</y>
      <width>47</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QSpinBox" name="spinBoxFinalTopomap">
    <property name="geometry">
     <rect>
      <x>410</x>
      <y>150</y>
      <width>47</width>
      <height>24</height>
     </rect>
    </property>
   </widget>
   <widget class="QFrame" name="frame_4">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>220</y>
      <width>431</width>
      <height>131</height>
     </rect>
    </property>
    <property name="frameShape">
     <enum>QFrame::StyledPanel</enum>
    </property>
    <property name="frameShadow">
     <enum>QFrame::Raised</enum>
    </property>
    <widget class="QLabel" name="label_7">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>20</y>
       <width>81</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Initial time</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_8">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>60</y>
       <width>81</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Final time</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_9">
     <property name="geometry">
      <rect>
       <x>10</x>
       <y>100</y>
       <width>81</width>
       <height>16</height>
      </rect>
     </property>
     <property name="text">
      <string>Interval</string>
     </property>
    </widget>
    <widget class="QDoubleSpinBox" name="SpinBoxInitialTimeTopomap">
     <property name="geometry">
      <rect>
       <x>90</x>
       <y>10</y>
       <width>66</width>
       <height>31</height>
      </rect>
     </property>
     <property name="decimals">
      <number>3</number>
     </property>
     <property name="minimum">
      <double>-2.000000000000000</double>
     </property>
     <property name="maximum">
      <double>4.000000000000000</double>
     </property>
     <property name="singleStep">
      <double>0.010000000000000</double>
     </property>
     <property name="value">
      <double>-0.500000000000000</double>
     </property>
    </widget>
    <widget class="QDoubleSpinBox" name="SpinBoxFinalTimeTopomap">
     <property name="geometry">
      <rect>
       <x>90</x>
       <y>50</y>
       <width>66</width>
       <height>31</height>
      </rect>
     </property>
     <property name="decimals">
      <number>3</number>
     </property>
     <property name="minimum">
      <double>-2.000000000000000</double>
     </property>
     <property name="maximum">
      <double>4.000000000000000</double>
     </property>
     <property name="singleStep">
      <double>0.010000000000000</double>
     </property>
     <property name="value">
      <double>1.000000000000000</double>
     </property>
    </widget>
    <widget class="QDoubleSpinBox" name="SpinBoxIntervalTopomap">
     <property name="geometry">
      <rect>
       <x>90</x>
       <y>90</y>
       <width>66</width>
       <height>31</height>
      </rect>
     </property>
     <property name="decimals">
      <number>3</number>
     </property>
     <property name="maximum">
      <double>1.000000000000000</double>
     </property>
     <property name="singleStep">
      <double>0.005000000000000</double>
     </property>
     <property name="value">
      <double>0.300000000000000</double>
     </property>
    </widget>
    <widget class="QLabel" name="label_13">
     <property name="geometry">
      <rect>
       <x>165</x>
       <y>20</y>
       <width>67</width>
       <height>15</height>
      </rect>
     </property>
     <property name="text">
      <string>Vmax(mV)</string>
     </property>
    </widget>
    <widget class="QLabel" name="label_14">
     <property name="geometry">
      <rect>
       <x>165</x>
       <y>60</y>
       <width>67</width>
       <height>15</height>
      </rect>
     </property>
     <property name="text">
      <string>Vmin(mV)</string>
     </property>
    </widget>
    <widget class="QDoubleSpinBox" name="doubleSpinBoxVmax">
     <property name="geometry">
      <rect>
       <x>234</x>
       <y>10</y>
       <width>66</width>
       <height>31</height>
      </rect>
     </property>
     <property name="decimals">
      <number>1</number>
     </property>
     <property name="minimum">
      <double>-500.000000000000000</double>
     </property>
     <property name="maximum">
      <double>500.000000000000000</double>
     </property>
     <property name="singleStep">
      <double>10.000000000000000</double>
     </property>
     <property name="value">
      <double>80.000000000000000</double>
     </property>
    </widget>
    <widget class="QDoubleSpinBox" name="doubleSpinBoxVmin">
     <property name="geometry">
      <rect>
       <x>234</x>
       <y>50</y>
       <width>66</width>
       <height>31</height>
      </rect>
     </property>
     <property name="decimals">
      <number>1</number>
     </property>
     <property name="minimum">
      <double>-500.000000000000000</double>
     </property>
     <property name="maximum">
      <double>500.000000000000000</double>
     </property>
     <property name="singleStep">
      <double>10.000000000000000</double>
     </property>
     <property name="value">
      <double>-80.000000000000000</double>
     </property>
    </widget>
    <widget class="QRadioButton" name="radioButtonChNames">
     <property name="geometry">
      <rect>
       <x>165</x>
       <y>90</y>
       <width>131</width>
       <height>31</height>
      </rect>
     </property>
     <property name="text">
      <string>Show Ch names</string>
     </property>
     <property name="autoExclusive">
      <bool>false</bool>
     </property>
    </widget>
    <widget class="QLabel" name="label_10">
     <property name="geometry">
      <rect>
       <x>311</x>
       <y>17</y>
       <width>31</width>
       <height>20</height>
      </rect>
     </property>
     <property name="text">
      <string>Size</string>
     </property>
    </widget>
    <widget class="QSpinBox" name="spinBoxTopoSize">
     <property name="geometry">
      <rect>
       <x>370</x>
       <y>10</y>
       <width>48</width>
       <height>31</height>
      </rect>
     </property>
     <property name="minimum">
      <number>1</number>
     </property>
     <property name="maximum">
      <number>10</number>
     </property>
     <property name="value">
      <number>2</number>
     </property>
    </widget>
    <widget class="QLabel" name="label_15">
     <property name="geometry">
      <rect>
       <x>311</x>
       <y>60</y>
       <width>59</width>
       <height>15</height>
      </rect>
     </property>
     <property name="text">
      <string>Contours</string>
     </property>
    </widget>
    <widget class="QSpinBox" name="spinBoxContours">
     <property name="geometry">
      <rect>
       <x>370</x>
       <y>50</y>
       <width>47</width>
       <height>30</height>
      </rect>
     </property>
     <property name="maximum">
      <number>30</number>
     </property>
     <property name="value">
      <number>6</number>
     </property>
    </widget>
    <widget class="QRadioButton" name="radioButtonBoundary">
     <property name="geometry">
      <rect>
       <x>310</x>
       <y>95</y>
       <width>121</width>
       <height>21</height>
      </rect>
     </property>
     <property name="text">
      <string>Show Outlines</string>
     </property>
     <property name="checked">
      <bool>true</bool>
     </property>
     <property name="autoExclusive">
      <bool>false</bool>
     </property>
    </widget>
   </widget>
   <widget class="QLabel" name="label_6">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>200</y>
      <width>131</width>
      <height>16</height>
     </rect>
    </property>
    <property name="text">
     <string>Plotting features</string>
    </property>
   </widget>
  </widget>
  <widget class="QPushButton" name="ButtonClearFigures">
   <property name="geometry">
    <rect>
     <x>360</x>
     <y>50</y>
     <width>101</width>
     <height>41</height>
    </rect>
   </property>
   <property name="palette">
    <palette>
     <active>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>239</red>
         <green>56</green>
         <blue>31</blue>
        </color>
       </brush>
      </colorrole>
     </active>
     <inactive>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>239</red>
         <green>56</green>
         <blue>31</blue>
        </color>
       </brush>
      </colorrole>
     </inactive>
     <disabled>
      <colorrole role="Button">
       <brush brushstyle="SolidPattern">
        <color alpha="255">
         <red>239</red>
         <green>56</green>
         <blue>31</blue>
        </color>
       </brush>
      </colorrole>
     </disabled>
    </palette>
   </property>
   <property name="text">
    <string>Close Figures</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Button2PDF">
   <property name="geometry">
    <rect>
     <x>360</x>
     <y>135</y>
     <width>41</width>
     <height>19</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(85, 255, 127);</string>
   </property>
   <property name="text">
    <string>PDF</string>
   </property>
  </widget>
  <widget class="QPushButton" name="Button2PNG">
   <property name="geometry">
    <rect>
     <x>421</x>
     <y>136</y>
     <width>41</width>
     <height>19</height>
    </rect>
   </property>
   <property name="styleSheet">
    <string notr="true">background-color: rgb(85, 255, 127);</string>
   </property>
   <property name="text">
    <string>PNG</string>
   </property>
  </widget>
  <widget class="QLabel" name="label_16">
   <property name="geometry">
    <rect>
     <x>368</x>
     <y>113</y>
     <width>89</width>
     <height>16</height>
    </rect>
   </property>
   <property name="text">
    <string>Export Figures</string>
   </property>
  </widget>
  <widget class="QFrame" name="frame">
   <property name="geometry">
    <rect>
     <x>349</x>
     <y>130</y>
     <width>121</width>
     <height>31</height>
    </rect>
   </property>
   <property name="frameShape">
    <enum>QFrame::StyledPanel</enum>
   </property>
   <property name="frameShadow">
    <enum>QFrame::Raised</enum>
   </property>
  </widget>
  <zorder>frame</zorder>
  <zorder>framePlottingEvoked</zorder>
  <zorder>frame_2</zorder>
  <zorder>label</zorder>
  <zorder>frameEpochs</zorder>
  <zorder>label_2</zorder>
  <zorder>ButtonClearFigures</zorder>
  <zorder>Button2PDF</zorder>
  <zorder>Button2PNG</zorder>
  <zorder>label_16</zorder>
 </widget>
 <resources/>
 <connections/>
</ui>