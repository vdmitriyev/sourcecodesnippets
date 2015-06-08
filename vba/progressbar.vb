' Just a line that changes during the slides
Sub AddProgressBar01()
    On Error Resume Next
        With ActivePresentation
			margin_right = 44
			margin_left = 22
			margin_bottom = 30			
			bar_width = 9
			
			For X = 1 To .Slides.Count
				' delete object from slides
				.Slides(X).Shapes("PB").Delete
				Set s = .Slides(X).Shapes.AddShape(msoShapeRectangle, _
						margin_left, _
						.PageSetup.SlideHeight - margin_bottom, _
						X * .PageSetup.SlideWidth / .Slides.Count, _
						bar_width)
				Call s.Fill.Solid
				s.Line.Visible = False
				s.Fill.ForeColor.RGB = RGB(192, 192, 192)
				s.Name = "PB"
		  Next X:
        End With
End Sub


' Two lines with different colours
Sub AddProgressBar02()
    On Error Resume Next
        With ActivePresentation
		
			margin_right = 44
			margin_left = 22
			margin_bottom = 30			
			bar_width = 9
			
            For X = 2 To .Slides.Count - 2
			
				.Slides(X).Shapes("PB").Delete
              
				Set s = .Slides(X).Shapes.AddShape(msoShapeRectangle, _
						margin_left, _
						.PageSetup.SlideHeight - margin_bottom, _
						X * .PageSetup.SlideWidth / .Slides.Count, _
						bar_width)
				Call s.Fill.Solid
				s.Line.Visible = True
				s.Fill.ForeColor.RGB = RGB(192, 192, 192)
				s.Name = "PB"
              
				.Slides(X).Shapes("PB1").Delete
				Set f = .Slides(X).Shapes.AddShape(msoShapeRectangle, _
						margin_left + (X * .PageSetup.SlideWidth / .Slides.Count), _
						.PageSetup.SlideHeight - margin_bottom, _
						.PageSetup.SlideWidth - (X * .PageSetup.SlideWidth / .Slides.Count) - margin_right, _
						bar_width)
				Call f.Fill.Solid
				
				f.Line.Visible = False
				f.Fill.ForeColor.RGB = RGB(192, 192, 192)
				f.Name = "PB1"
              Next X:
        End With
End Sub

' Line that contains different boxes
Sub AddProgressBar()
    On Error Resume Next
        With ActivePresentation
			Dim str_slide_name As String
			
			margin_left = 21
			margin_bottom = 30
			single_bar_width = (.PageSetup.SlideWidth - margin_left - 1) / .Slides.Count              
			bar_width = 9
			  
            N = .Slides.Count - 1
              
            For X = 2 To N        
			
                For I = 0 To X - 1				
					'name of the object
					slide_name = "PB" & I					
					'removing previous object from slide
					.Slides(X).Shapes(slide_name).Delete
					'creating the
					Set s = .Slides(X).Shapes.AddShape(msoShapeRectangle, _
							margin_left + I * single_bar_width, _
							.PageSetup.SlideHeight - margin_bottom, _
							single_bar_width, bar_width)
                  
					Call s.Fill.Solid
					s.Line.Visible = True
					s.Fill.ForeColor.RGB = RGB(0, 192, 0)
                  
					s.Name = slide_name
                 Next I:
                 
                 For I = X To N - 1
					' name of the object
					slide_name = "PB_" & I
					' removing previous object from slide
					.Slides(X).Shapes(str_slide_name).Delete
                  
					Set s = .Slides(X).Shapes.AddShape(msoShapeRectangle, _
							margin_left + I * single_bar_width, _
							.PageSetup.SlideHeight - margin_bottom, _
							single_bar_width, bar_width)
                  
					Call s.Fill.Solid
					s.Line.Visible = True
					s.Fill.ForeColor.RGB = RGB(0, 255, 255)
                  
					s.Name = slide_name
                 Next I:
               
            Next X:
        End With
End Sub