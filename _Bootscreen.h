/**
 * Marlin 3D Printer Firmware
 * Copyright (c) 2020 MarlinFirmware [https://github.com/MarlinFirmware/Marlin]
 *
 * Based on Sprinter and grbl.
 * Copyright (c) 2011 Camiel Gubbels / Erik van der Zalm
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <https://www.gnu.org/licenses/>.
 *
 */
#pragma once

#define CUSTOM_BOOTSCREEN_ANIMATED
#define CUSTOM_BOOTSCREEN_TIMEOUT 0                 // (ms) Extra timeout after the animation

/**
 * Enable one of the following two options depending on your needs.
 * Also edit the "custom_bootscreen_animation" at the bottom of this file.
*/
#define CUSTOM_BOOTSCREEN_FRAME_TIME 200            // (ms) Same time for all frames
//#define CUSTOM_BOOTSCREEN_ANIMATED_FRAME_TIME     // Each frame also has a duration    

#define CUSTOM_BOOTSCREEN_BMPWIDTH 128
