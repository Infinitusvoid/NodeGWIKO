// ----

float rand(vec2 co)
{
    return fract(sin(dot(co, vec2(12.9898, 78.233))) * 43758.5453);
}

vec3 palette( in float t, in vec3 a, in vec3 b, in vec3 c, in vec3 d )
{
    return a + b*cos( 6.28318*(c*t+d) );
}


vec3 palette_0(float t)
{
  return palette (
  t,
  pallete_0_a,
  pallete_0_b,
  pallete_0_c,
  pallete_0_d
  );
}

vec3 palette_1(float t)
{
  return palette (
  t,
  pallete_1_a,
  pallete_1_b,
  pallete_1_c,
  pallete_1_d
  );
}


float f_texture_0_t_f(float t)
{
 return t * f_texture_0_t_f_multiplication_value;
}

float f_texture_1_t_f(float t)
{
 return t * f_texture_1_t_f_multiplication_value;
}


float f_texture_2x_t_f(float t)
{
 return t * f_texture_2x_t_f_multiplication_value;
}


// texture 0

float f_texture_0_r(vec3 uvt) 
{
  float u = uvt[0];
  float v = uvt[1];
  float t = uvt[2];
  return 0.24 * sin(u * 10.0 + t * 0.72 + 0.2 * sin(v * 10.0 + t));
}

float f_texture_0_g(vec3 uvt) 
{
  float u = uvt[0];
  float v = uvt[1];
  float t = uvt[2];
  return sin(u * 10.0 + t * 0.2);
}

float f_texture_0_b(vec3 uvt) 
{
  float u = uvt[0];
  float v = uvt[1];
  float t = uvt[2];
  return sin(u * 10.0 + t * 0.42);
}

vec3 f_texture_0_rgb(vec3 uvt, vec3 rgb) 
{
  float u = uvt[0];
  float v = uvt[1];
  float t = uvt[2];
  return vec3(rgb[0], rgb[1], rgb[2]);
}

// texture 1

vec4 f_texture_1(vec3 uvt)
{
  float u = uvt[0];
  float v = uvt[1];
  float t = f_texture_0_t_f(uvt[2]);

  
  vec2 id = round(vec2(u, v)/texture_0_s0);
  vec2 uv_0 = vec2(u, v) - texture_0_s0 * id; 

  float u_0 = 0.5 +  uv_0[0] * (1.0 / texture_0_s0[0]);
  float v_0 = 0.5 +  uv_0[1] * (1.0 / texture_0_s0[0]);
  
  
  float tt = round(t);
  float offset = rand(vec2(float(id.x) * 44.7 + tt, float(id.y) * 73.24 + tt));
  float value = rand(vec2(float(id.x) * 234.7 + offset, float(id.y) * 417.24 + offset));

  vec3 color = palette_0(value);
  
  // vec2 r = p - s*id;
  //  return sdf(r, id);

  
  float r = u_0 * color[0];
  float g = u_0 * color[1]; // color.g;
  float b = u_0 * color[2]; // color.b;
  
  
  return vec4(r, g, b, 1.0);
}


vec3 f_texture_2_mixture(vec3 color, vec3 color_tex_1, vec3 uvt)
{
  float u_0 = uvt[0];
  float v_0 = uvt[1];
  float t_0 = uvt[2];

  
  // red
  
  float fru = 1.0;
  fru += abs(fru_amp_0 * sin(t_0 * fru_freq_0));
  fru += abs(fru_amp_1 * sin(t_0 * fru_freq_1));
  fru += abs(fru_amp_2 * sin(t_0 * fru_freq_2));
  fru += abs(fru_amp_3 * sin(t_0 * fru_freq_3));
  fru += abs(fru_amp_4 * sin(t_0 * fru_freq_4));
  fru += abs(fru_amp_5 * sin(t_0 * fru_freq_5));
  fru += abs(fru_amp_6 * sin(t_0 * fru_freq_6));
  fru += abs(fru_amp_7 * sin(t_0 * fru_freq_7));
  
  float frv = 1.0;
  frv += abs(frv_amp_0 * sin(t_0 * frv_freq_0));
  frv += abs(frv_amp_1 * sin(t_0 * frv_freq_1));
  frv += abs(frv_amp_2 * sin(t_0 * frv_freq_2));
  frv += abs(frv_amp_3 * sin(t_0 * frv_freq_3));
  frv += abs(frv_amp_4 * sin(t_0 * frv_freq_4));
  frv += abs(frv_amp_5 * sin(t_0 * frv_freq_5));
  frv += abs(frv_amp_6 * sin(t_0 * frv_freq_6));
  frv += abs(frv_amp_7 * sin(t_0 * frv_freq_7));
  
  
  
  float r = 0.0;
  r += u_0 * color[0] * f_texture_2_mixture_r_u_0_factor * (fru_mult * fru);
  r += v_0 * color[0] * f_texture_2_mixture_r_v_0_factor * (frv_mult * frv);
  r *= color_tex_1[0]; 
  
  
  // green
  
  float fgu = fgu_offset;
  fgu += abs(fgu_amp_0 * sin(t_0 * fgu_freq_0));
  fgu += abs(fgu_amp_1 * sin(t_0 * fgu_freq_1));
  fgu += abs(fgu_amp_2 * sin(t_0 * fgu_freq_2));
  fgu += abs(fgu_amp_3 * sin(t_0 * fgu_freq_3));
  fgu += abs(fgu_amp_4 * sin(t_0 * fgu_freq_4));
  fgu += abs(fgu_amp_5 * sin(t_0 * fgu_freq_5));
  fgu += abs(fgu_amp_6 * sin(t_0 * fgu_freq_6));
  fgu += abs(fgu_amp_7 * sin(t_0 * fgu_freq_7));
  
  float fgv = fgv_offset;
  fgv += abs(fgv_amp_0 * sin(t_0 * fgv_freq_0));
  fgv += abs(fgv_amp_1 * sin(t_0 * fgv_freq_1));
  fgv += abs(fgv_amp_2 * sin(t_0 * fgv_freq_2));
  fgv += abs(fgv_amp_3 * sin(t_0 * fgv_freq_3));
  fgv += abs(fgv_amp_4 * sin(t_0 * fgv_freq_4));
  fgv += abs(fgv_amp_5 * sin(t_0 * fgv_freq_5));
  fgv += abs(fgv_amp_6 * sin(t_0 * fgv_freq_6));
  fgv += abs(fgv_amp_7 * sin(t_0 * fgv_freq_7));
  
  
  float g = 0.0;
  g += u_0 * color[1] * f_texture_2_mixture_g_u_0_factor * (fgu_mult * fgu);
  g += v_0 * color[1] * f_texture_2_mixture_g_v_0_factor * (fgv_mult * fgv);
  g *= color_tex_1[1]; 
  
  
  // blue
  
  float fbu = fbu_offset;
  fbu += abs(fbu_amp_0 * sin(t_0 * fbu_freq_0));
  fbu += abs(fbu_amp_1 * sin(t_0 * fbu_freq_1));
  fbu += abs(fbu_amp_2 * sin(t_0 * fbu_freq_2));
  fbu += abs(fbu_amp_3 * sin(t_0 * fbu_freq_3));
  fbu += abs(fbu_amp_4 * sin(t_0 * fbu_freq_4));
  fbu += abs(fbu_amp_5 * sin(t_0 * fbu_freq_5));
  fbu += abs(fbu_amp_6 * sin(t_0 * fbu_freq_6));
  fbu += abs(fbu_amp_7 * sin(t_0 * fbu_freq_7));
  
  float fbv = fbv_offset;
  fbv += abs(fbv_amp_0 * sin(t_0 * fbv_freq_0));
  fbv += abs(fbv_amp_1 * sin(t_0 * fbv_freq_1));
  fbv += abs(fbv_amp_2 * sin(t_0 * fbv_freq_2));
  fbv += abs(fbv_amp_3 * sin(t_0 * fbv_freq_3));
  fbv += abs(fbv_amp_4 * sin(t_0 * fbv_freq_4));
  fbv += abs(fbv_amp_5 * sin(t_0 * fbv_freq_5));
  fbv += abs(fbv_amp_6 * sin(t_0 * fbv_freq_6));
  fbv += abs(fbv_amp_7 * sin(t_0 * fbv_freq_7));
  
  float b = 0.0;
  b += u_0 * color[2] * f_texture_2_mixture_b_u_0_factor * (fbu_mult * fbu);
  b += v_0 * color[2] * f_texture_2_mixture_b_v_0_factor * (fbv_mult * fbv);
  b *= color_tex_1[2];
  
  return vec3(r, g, b);
}


vec4 f_texture_2(vec3 uvt)
{
  float u = uvt[0];
  float v = uvt[1];
  float t = f_texture_1_t_f(uvt[2]);

  // space repetition
  
  vec2 id = round(vec2(u, v)/texture_1_s0);
  vec2 uv_0 = vec2(u, v) - texture_1_s0 * id; 

  float u_0 = 0.5 +  uv_0[0] * (1.0 / texture_1_s0[0]);
  float v_0 = 0.5 +  uv_0[1] * (1.0 / texture_1_s0[0]);
  
  
  float tt = round(t);
  float offset = rand(vec2(float(id.x) * 421.7  + tt, float(id.y)    * 432.24  + tt    ));
  float value_rnd =  rand(vec2(float(id.x) * 234.7 + offset, float(id.y) * 417.24 + offset));
  
  vec3 color = palette_1(value_rnd);
  
  
  
  vec4 tex_1 = vec4(1.0, 1.0, 1.0, 1.0);
  
  if( rand(vec2(float(id.x) * 424.4 + tt, float(id.y) * 34.42 + tt)) > f_texture_2_mixture_2_to_1)
  {
     tex_1 = f_texture_1(vec3(u_0, v_0, t));
  }
  
  
  vec3 rgb = f_texture_2_mixture(color, vec3(tex_1[0], tex_1[1], tex_1[2]), vec3(u_0, v_0, t));
  return vec4(rgb, 1.0);
}


vec4 option_0(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = v0 + v1;
    
    if(sin(u  * 20.0 + sin(t*v * 0.2)) > sin(v * 20.0 + sin(t*u* 0.2)))
    {
       value_out *= v0 * v1;
    }
    
    return value_out;
}


vec4 option_1(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = v0 + v1;
    
    if(sin(u  * 20.0 + sin(t*v * 0.2)) > sin(v * 20.0 + sin(t*u* 0.2)))
    {
       value_out += sin((v0/v1) * 0.1);
    }
    
    return value_out;
}


vec4 option_2(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = v0 + v1;
    
    if(sin(u  * (20.0 * option_2_parameter_0) + sin(t*v * 0.2 * option_2_parameter_2)) > sin(v * (20.0 * option_2_parameter_1) + sin(t*u* 0.4 * option_2_parameter_3)))
    {
       value_out = v1 + 0.42 * (v0 / v1) * sin(u * 10.0 + t + v * sin(t * 64.0 * (1.0 + 0.4 * sin(t + v * 72.0)) + u * 42.0));
    }
    
    return value_out;
}


vec4 option_3(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = v0 * v1;
    
    if(sin(u  * (20.0 * option_2_parameter_0) + sin(t*v * 0.2 * option_2_parameter_2)) > sin(v * (20.0 * option_2_parameter_1) + sin(t*u* 0.4 * option_2_parameter_3)))
    {
       value_out += (v1 - v0);
    }
    
    return value_out;
}


vec4 option_4(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = v0;
    
    value_out = 1.0 / (abs(v0) + abs(v1) + 0.01);
    value_out = log(value_out);
    
    value_out *= 0.2 * option_4_paramter_3;
    
    vec4 vv = vec4(1.0, 1.0, 1.0, 1.0);
    vv *= vec4(palette_0( abs(sin(value_out.r * 10.0 * option_4_paramter_0)) ), 1.0);
    vv *= vec4(palette_0( abs(sin(value_out.g * 10.0 * option_4_paramter_1)) ), 1.0);
    vv *= vec4(palette_0( abs(sin(value_out.b * 10.0 * option_4_paramter_0)) ), 1.0);
    
    value_out += vv * 0.2 * option_4_paramter_4;
    
    
    value_out = abs(value_out);
    return value_out;
}


vec4 option_5(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 vv0 = f_texture_2x_f0_amplitude * sin(v0 / v1) + cos(v0 * v1 * f_texture_2x_frequency_0 * u * sin(t + u)) * 0.2;
    vec4 vv1 = vec4( abs(fract(vec3(v0) * vec3(v1) * 10.0 * option_5_paramter_0)), 1.0);
    
    return mix(vv0, vv1, option_5_paramter_1);
}


vec4 option_6(vec4 v0, vec4 v1, float u, float v, float t)
{
    return option_5(v0, v1, u, v, t) * option_4(v0, v1, u, v, t) * 4.0;
}



vec4 option_7(vec4 v0, vec4 v1, float u, float v, float t)
{
    vec4 value_out = option_0(v0, v1, u, v, t) * abs(sin(option_0(v0, v1, u, v, t) / option_5(v0, v1, u, v, t)));
    value_out = abs(value_out);
    value_out +=  0.2 * option_5(v0, v1, u, v, t) * option_7_paramter_0;
    value_out +=  0.2 * option_1(v0, v1, u, v, t) * option_7_paramter_1;
    return value_out;
}




vec4 f_texture_2x(vec3 uvt)
{
  float u = uvt[0];
  float v = uvt[1];
  float t = f_texture_2x_t_f(uvt[2]);

  vec4 v0 = mix(f_texture_2(vec3(u, v, t)), f_texture_2(vec3(u, v, t + 1.0)), pow(fract(t), 2.0));
  vec4 v1 = mix(f_texture_2(vec3(u, v, t + 2.0)), f_texture_2(vec3(u, v, t + 3.0)), pow(fract(t), 2.0));
  
  
  vec4 value_out = USE_FUNCTION(v0, v1, u, v, t);
  
  return  value_out;
  
}




/*
void main()
{
    // Adjusting for screen ratio
    ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);
    vec2 iResolution = vec2(1980.0, 1080);

    vec2 uv = pixel_coords.xy / iResolution.xy;
    uv.x *= iResolution.x / iResolution.y;  // Compensate for screen ratio

    


    float iTime = 1.0;

    float value_t =  (parameter_t_offset * 1000.0) + parameter_t_amplitude * 1000.0 * sin(iTime * 0.0024 * parameter_t_frequency);
    
    
    vec3 col = vec3(0.0, 0.0, 0.0);
    
    vec4 v_1 = f_texture_2x(vec3(uv, value_t));
    
    col = vec3(v_1[0], v_1[1], v_1[2]);
    
    
    //Time varying pixel color
    col += (0.5 + 0.5 * cos(value_t + uv.xyx + vec3(0, 2, 4))) * 0.1 * parameter_time_varying_pixel_color;

    // Add a moving gradient based on time
    col += (0.5 * cos(value_t * 0.5) * vec3(uv, 1.0 - uv)) * 0.1 * parameter_add_a_moving_gradient_based_on_time;
    

    // Apply post-processing effects
    // col = col * 1.5 - 0.25; // Increase overall brightness
    col = col * (1.0 - parameter_apply_post_processing_effects) +  pow(col, vec3(1.2)) * parameter_apply_post_processing_effects; // Apply gamma correction

    // Output to screen
    fragColor = vec4(col, 1.0);
}
*/


void main()
{
  ivec2 pixel_coords = ivec2(gl_GlobalInvocationID.xy);
  vec2 iResolution = vec2(1980.0, 1080);

   vec2 uv = pixel_coords.xy / iResolution.xy;
    uv.x *= iResolution.x / iResolution.y;  // Compensate for screen ratio

    float iTime = float(int_frame) / 60.0;

    float value_t =  (parameter_t_offset * 1000.0) + parameter_t_amplitude * 1000.0 * sin(iTime * 0.0024 * parameter_t_frequency);
    
    
    vec3 col = vec3(0.0, 0.0, 0.0);
    
    vec4 v_1 = f_texture_2x(vec3(uv, value_t));
    
    col = vec3(v_1[0], v_1[1], v_1[2]);
    
    //Time varying pixel color
    col += (0.5 + 0.5 * cos(value_t + uv.xyx + vec3(0, 2, 4))) * 0.1 * parameter_time_varying_pixel_color;

    // Add a moving gradient based on time
    col += (0.5 * cos(value_t * 0.5) * vec3(uv, 1.0 - uv)) * 0.1 * parameter_add_a_moving_gradient_based_on_time;
    

    // Apply post-processing effects
    // col = col * 1.5 - 0.25; // Increase overall brightness
    col = col * (1.0 - parameter_apply_post_processing_effects) +  pow(col, vec3(1.2)) * parameter_apply_post_processing_effects; // Apply gamma correction
 
  // vec4 color = vec4(pixel_coords.x / 1920.0, pixel_coords.y / 1080.0, 0.0, 1.0);
  // color.g = color.g + float(int_frame) * 0.01;
  // color.r *= 0.74;


  vec4 color = vec4(col, 1.0);
  imageStore(out0, pixel_coords, color);
}