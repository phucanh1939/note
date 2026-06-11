---
title: Image
---

# Image 

## What is an Image

An image is a visual representation of light properties (color, brightness, contrast) that captures how light interacts with objects in a scene at a specific moment. It can also be created or manipulated through artistic, digital, or photographic processes to represent a scene, idea, or concept.

**Images** can be **analog** (paintings, photographs) or **digital** (bitmap, vector graphics)

**A digital image** is a representation of an image using discrete numerical values, typically stored as a grid of pixels. Each pixel represents a sample of the scene or object being depicted, and its numerical value encodes properties such as brightness and color.

## Types of Digital Images

| **Type** | **Definition** | **Representation in Binary** | **Best For** | **Formats** |
|------------|-------------|--------------------|------------|------------|
| **Raster (Bitmap)** | Made of individual pixels, each storing color information. Fixed resolution, loses quality when scaled. | Stored as a grid of pixel values, where each pixel has color channels (e.g., RGB: 8-bit per channel = 24-bit per pixel). | Photos, digital art | JPEG, PNG, GIF, BMP, TIFF |
| **Vector** | Uses mathematical formulas to define shapes, lines, and colors. Infinitely scalable without losing quality. | Described using geometric formulas (points, lines, curves) stored as mathematical expressions instead of pixel data. | Logos, icons, illustrations | SVG, AI, EPS, PDF |
| **3D Images** | Represents 3D objects using meshes, textures, and lighting. Used in 3D modeling and rendering. | Meshes: Stored as lists of vertices and edges. Textures: Stored as raster images mapped onto the surface. Lighting: Stored as mathematical models. | Games, animation, 3D printing | OBJ, FBX, STL |
| **HDR Images** | Stores a wider range of brightness and color data for high-quality lighting and shading. Used in photography and VFX. | Uses **floating-point precision** (e.g., 16-bit or 32-bit per channel) to store high dynamic range pixel values instead of standard 8-bit integers. | Photography, cinema, gaming | HDR, EXR |

## How to Represent a Raster Image in Binary

### Representation

- An Raster Image is represent in computer using tiny dots (**pixels**) arranged in a grid.

- Each pixel has a **color** value, represented in binary using diferrent **color models**.

- The **color** value of a **pixel** is an **approximation** because computers use a limited number of bits to represent a continuous range of colors, just like [floating-point] numbers approximate real [numbers].

#### What is a Color

**Color** is the perception of different wavelengths of light by the human eye and brain.

It is a visual property that arises when light interacts with objects and is either absorbed, reflected, or emitted.

**Example:** A wavelength of 495 nm can be mapped to a color value, approximated as #00FF00 in a 24-bit RGB representation.

#### Common Color Models

| **Color Model** | **Idea (Channels & Meaning)** | **Use Case** |
|---------------|--------------------------------|-------------|
| **RGB** (Red, Green, Blue) | Additive model; combines light to form colors. Each channel represents intensity of red, green, and blue (0–255 for 8bit each channel). | Digital screens (monitors, TVs, cameras). |
| **CMYK** (Cyan, Magenta, Yellow, Black) | Subtractive model; absorbs light. Cyan, Magenta, Yellow control color, Black (K) adds depth. | Printing (magazines, paper). |
| **HSL** (Hue, Saturation, Lightness) | Hue (color, 0°–360°), Saturation (color intensity, 0%–100%), Lightness (brightness, 0%–100%). | Graphic design, color selection. |
| **HSV** (Hue, Saturation, Value) | Similar to HSL, but Value represents brightness differently. | Image editing, UI design. |
| **YUV / YCbCr** | Y (Luminance), U/Cb (Blue Chrominance), V/Cr (Red Chrominance). Separates brightness from color. | Video compression (JPEG, MPEG, HDTV). |
| **LAB (CIELAB)** | L (Lightness), A (Green–Red), B (Blue–Yellow). Designed to match human vision. | High-precision color correction, photography. |  

### Common Image Formats

| **Format** | **Type**        | **Compression**     | **Transparency** | **Best For**                                |
|------------|-----------------|---------------------|------------------|---------------------------------------------|
| **JPEG**   | Raster (Bitmap) | Lossy               | No               | Photos, web images, when file size is a concern |
| **PNG**    | Raster (Bitmap) | Lossless            | Yes              | Web graphics, logos, images requiring transparency |
| **GIF**    | Raster (Bitmap) | Lossless            | Yes              | Simple animations, small graphics with limited colors (256) |
| **BMP**    | Raster (Bitmap) | Uncompressed         | No               | Basic bitmap images, low-quality graphics, Windows-specific |
| **TIFF**   | Raster (Bitmap) | Lossless (Can be lossy too) | Yes              | High-quality images, scanning, printing, medical imaging |
| **WebP**   | Raster (Bitmap) | Both Lossy & Lossless| Yes              | Web images (more efficient than JPEG/PNG) |
| **HEIF**   | Raster (Bitmap) | Both Lossy & Lossless| Yes              | Modern format for photos, supports high quality and small size |
| **SVG**    | Vector           | Lossless            | Yes              | Scalable graphics for logos, illustrations, web design |
| **EPS**    | Vector           | Lossless            | Yes              | Vector images, printing, and illustrations |
| **PDF**    | Vector or Raster | Lossless            | Yes              | Documents with images, graphics, and text |


#### Example: a 10x10 White image in 24-bit RPG data

```bash
# View the raw binary data of an image in BMP format
$ xxd images/White_10x10.bmp  
00000000: 424d 1a02 0000 0000 0000 8a00 0000 7c00  BM............|.
00000010: 0000 0a00 0000 0a00 0000 0100 2000 0300  ............ ...
00000020: 0000 9001 0000 c30e 0000 c30e 0000 0000  ................
00000030: 0000 0000 0000 0000 ff00 00ff 0000 ff00  ................
00000040: 0000 0000 00ff 4247 5273 8fc2 f528 51b8  ......BGRs...(Q.
00000050: 1e15 1e85 eb01 3333 3313 6666 6626 6666  ......333.fff&ff
00000060: 6606 9999 9909 3d0a d703 285c 8f32 0000  f.....=...(\.2..
00000070: 0000 0000 0000 0000 0000 0400 0000 0000  ................
00000080: 0000 0000 0000 0000 0000 ffff ffff ffff  ................
00000090: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000a0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000b0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000c0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000d0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000e0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000000f0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000100: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000110: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000120: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000130: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000140: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000150: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000160: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000170: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000180: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000190: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001a0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001b0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001c0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001d0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001e0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
000001f0: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000200: ffff ffff ffff ffff ffff ffff ffff ffff  ................
00000210: ffff ffff ffff ffff ffff                 ..........
```

```bash
# View the raw binary data of an image in PNG format
$ xxd images/White_10x10.png
00000000: 8950 4e47 0d0a 1a0a 0000 000d 4948 4452  .PNG........IHDR
00000010: 0000 000a 0000 000a 0806 0000 008d 32cf  ..............2.
00000020: bd00 0000 0173 5247 4200 aece 1ce9 0000  .....sRGB.......
00000030: 0004 6741 4d41 0000 b18f 0bfc 6105 0000  ..gAMA......a...
00000040: 0009 7048 5973 0000 0ec3 0000 0ec3 01c7  ..pHYs..........
00000050: 6fa8 6400 0000 1749 4441 5428 5363 f84f  o.d....IDAT(Sc.O
00000060: 2460 4017 c005 4615 e205 442b 0400 23fb  $`@...F...D+..#.
00000070: 8e80 6985 5d2c 0000 0000 4945 4e44 ae42  ..i.],....IEND.B
00000080: 6082 
```

## History of Images

### Early Beginnings (Pre-19th Century)  
- Cave Paintings: Earliest visual representations (~30,000 years ago).  
- Ancient Art: Ancient Egyptians, Greeks, and Romans depicted gods and historical events.

### Invention of Photography (19th Century)  
- 1826: Joseph Nicéphore Niépce captured the first permanent photograph ("View from the Window at Le Gras").  
- 1839: Louis Daguerre developed the daguerreotype, the first commercially successful photographic process.  
- 1850s: Albumen prints and wet collodion process improved photographic clarity.  
- 1871: Richard Leach Maddox introduced the dry plate process, making photography portable.

### Color Photography and Film (20th Century)  
- 1907: Autochrome plate introduced the first commercial color photography process.  
- 1935: Kodachrome film became popular for vibrant color photographs.

### Modern Era (Digital Age - 21st Century)  
- Digital Photography (1990s–Present): Transition from film-based to digital photography with digital sensors (CCD, CMOS).  
- 2000s: Rise of smartphone cameras, making photography ubiquitous.  
- High-resolution sensors (e.g., 4K, 8K, and beyond) for sharper images.

### Image Editing and Software (1990s–Present)  
- Software like Adobe Photoshop revolutionized image editing and manipulation.  
- AI and Machine Learning now power many tools for automatic enhancement, deepfakes, and style transfers.

### 3D Imaging and Rendering (2000s–Present)  
- Advancements in 3D rendering technology for film, gaming, and virtual reality (VR).  
- Augmented Reality (AR) and Mixed Reality (MR) are increasingly using image data for immersive experiences.

### High Dynamic Range (HDR) and 3D Imaging  
- HDR imaging has become common in photography and cinema, providing better contrast and color range.  
- 3D scanning and printing continue to grow in popularity for entertainment, engineering, and manufacturing.

[floating-point]: FloatingPoint
[numbers]: Number

