#version 430
layout (local_size_x = 16, local_size_y = 16) in;
layout (binding = 0, rgba32f) uniform image2D input0;
layout (binding = 1, rgba32f) uniform image2D input1;
layout (binding = 2, rgba32f) uniform image2D input2;
layout (binding = 3, rgba32f) uniform image2D input3;
layout (binding = 4, rgba32f) uniform image2D out0;
layout (binding = 5, rgba32f) uniform image2D out1;
layout (binding = 6, rgba32f) uniform image2D out2;
layout (binding = 7, rgba32f) uniform image2D out3;
int int_frame = 0;
void main() {
   ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);
   vec4 color = vec4(pixel_coords.x / 1024.0, pixel_coords.y / 1024.0, 0.0, 1.0);
   vec4 color_image_0 = imageLoad(input0, pixel_coords);
   vec4 color_image_1 = imageLoad(input1, pixel_coords);
   imageStore(out0, pixel_coords, color);
   imageStore(out1, pixel_coords, vec4(0.0, 1.0, 0.0, 1.0));
   imageStore(out2, pixel_coords, color_image_1);
   imageStore(out3, pixel_coords, color_image_0);
}
