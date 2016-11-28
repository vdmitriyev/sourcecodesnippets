Option Explicit

Public Sub DeleteImagesOnSlides()
    Dim j As Integer, scount As Integer, fcount As Integer
    scount = ActivePresentation.Slides.Count
    Dim p As Long
    For j = 1 To scount
        fcount = ActivePresentation.Slides(j).Shapes.Count
        
        For p = fcount To 1 Step -1
            If ActivePresentation.Slides(j).Shapes(p).Type = msoPicture Then
			ActivePresentation.Slides(j).Shapes(p).Delete
            End If
        Next p
    Next j
End Sub


