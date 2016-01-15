Option Explicit
Public Sub ChangeFontOfSQLStatements()
    Dim j As Integer, k As Integer, scount As Integer, fcount As Integer
    Dim tr As TextRange
    Dim word As TextRange
    scount = ActivePresentation.Slides.Count
    For j = 1 To scount
        fcount = ActivePresentation.Slides(j).Shapes.Count
        For k = 1 To fcount
            If ActivePresentation.Slides(j).Shapes(k).HasTextFrame Then
                Set tr = ActivePresentation.Slides(j).Shapes(k).TextFrame.TextRange
                For Each word In tr.Words
                    If (StrComp(word, "select") = 0) Then
                    MsgBox CStr(word) 'just used this as a test
                        With tr
                            .Text = "!!!!!!!!!!!!!!1!"
                            .Words(1).Font.Bold = msoTrue
                            .Runs(1).Font.Italic = msoTrue
                            .Paragraphs(1).Font.Underline = msoTrue
                        End With
                    End If
                Next
            End If
        Next k
    Next j