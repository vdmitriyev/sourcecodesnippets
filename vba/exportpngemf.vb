
Sub ExportSingleDocument(ByVal directory As String, ByVal file_name As String)

    ' Open document in visio
    Dim vsoDoc As Document
    Set vsoDoc = Documents.Add(directory & "\" & file_name & ".vsd")
    
    ' Creating intermediate variables
    Dim vsoPage As Page
    Dim pngOutput As String
    Dim emfOutput As String
    
    ' Export each page as PNG
    For Each vsoPage In vsoDoc.Pages
    
      pngOutput = directory & "\png\" & vsoPage.Name & ".png"
      vsoPage.Export (pngOutput)
      
      emfOutput = directory & "\emf\" & vsoPage.Name & ".emf"
      vsoPage.Export (emfOutput)
    Next
    vsoDoc.Close
    
End Sub


Public Sub ExportAllVSOToPNGandEMF()

    ' Setting the quality of the output
    Application.Settings.SetRasterExportResolution visRasterUsePrinterResolution, 600#, 600#, visRasterPixelsPerInch
    
    ' Define directory to work in:
    Dim currentDirectory As String
    currentDirectory = CreateObject("Scripting.FileSystemObject").GetAbsolutePathName(".")
   
    ' Gather .vsd files in directory
    Dim vsoFilesCollection As New Collection
    Dim filename As String
    filename = Dir(currentDirectory & "\*.vsd")
   
    ' File names are stored without their extension
    Do While filename <> ""
        filename = Left(filename, InStrRev(filename, ".") - 1)
        If filename <> "Exporter" Then
            vsoFilesCollection.Add (filename)
        End If
        filename = Dir
    Loop
  
    ' Converting all pages in VISO files from collection to png and emf
    For Each vsoFile In vsoFilesCollection
        Call ExportSingleDocument(currentDirectory, vsoFile)
    Next
  
End Sub


Public Sub ExportOnlyCurrentVSOToPNGandEMF()

    ' Setting the quality of the output
    Application.Settings.SetRasterExportResolution visRasterUsePrinterResolution, 600#, 600#, visRasterPixelsPerInch
    
    ' Define directory to work in
    Dim currentDirectory As String
    currentDirectory = CreateObject("Scripting.FileSystemObject").GetAbsolutePathName(".")
    
    ' Selecting active VISIO file name
    activeVSOName = ActiveDocument.Name
    activeVSOName = Left(activeVSOName, InStrRev(activeVSOName, ".") - 1)
    
    ' Converting all pages in VISO file to png and emf
    Call ExportSingleDocument(currentDirectory, activeVSOName)
End Sub

