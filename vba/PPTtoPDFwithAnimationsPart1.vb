Sub AddElements()
Dim shp As Shape

Dim i As Integer, n As Integer
n = ActivePresentation.Slides.Count
For i = 1 To n
    Dim s As Slide
    Set s = ActivePresentation.Slides(i)
    s.SlideShowTransition.Hidden = msoTrue

    Dim max As Integer: max = 0
    For Each shp In s.Shapes
        If shp.AnimationSettings.Animate = msoTrue Then
            If shp.AnimationSettings.AnimationOrder > max Then
                max = shp.AnimationSettings.AnimationOrder
            End If
        End If
    Next

    Dim k As Integer, s2 As Slide
    For k = 0 To max
        Set s2 = s.Duplicate(1)
        s2.SlideShowTransition.Hidden = msoFalse
        s2.MoveTo ActivePresentation.Slides.Count

        Dim i2 As Integer
        For i2 = s2.Shapes.Count To 1 Step -1
            With s2.Shapes(i2)
                If .AnimationSettings.Animate = msoTrue Then
                    If .AnimationSettings.AnimationOrder > k Then
                        .Delete
                    Else
                        .AnimationSettings.Animate = msoFalse
                    End If
                End If
            End With
        Next
    Next
Next
End Sub

Sub RemElements()
Dim i As Integer, n As Integer
Dim s As Slide
n = ActivePresentation.Slides.Count
For i = n To 1 Step - 1
    Set s = ActivePresentation.Slides(i)
    If s.SlideShowTransition.Hidden = msoTrue Then
        s.SlideShowTransition.Hidden = msoFalse
    Else
        s.Delete
    End If
Next
End Sub
