# void DrawArc(float cx, float cy, float r, float start_angle, float arc_angle, int num_segments) 
# { 
#    GL.Begin(PrimitiveType.LineStrip);
#     double x = 2.047;
#     double y = 3.5;
#     double r = .5;
#     double start_angle = 1.5;
#     double end_angle = 3.2;
#     double max_angle = 2 * Math.PI;
#     double angle_increment = Math.PI / 1000;
#     for (double theta = start_angle; theta < end_angle; theta += angle_increment)
#     {

#         //x = r * Math.Cos (theta);
#         //y = r * Math.Sin (theta);
#         GL.Vertex2(x+  r * Math.Cos (theta), y+ r * Math.Sin (theta));
#     }
#     GL.End();
# }