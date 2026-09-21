<#
.SYNOPSIS  Render docs/deliverables/<key>.md to docs/deliverables/out/<Key>.docx with Pandoc.
.EXAMPLE   .\docs\deliverables\_template\build.ps1 pedagogy
           .\docs\deliverables\_template\build.ps1 all
.NOTES     Windows PowerShell 5.1 is enough. A documents tool, not a stack choice.
#>
param([Parameter(Mandatory = $true)][string]$Key)

$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot           # docs/deliverables
$outDir = Join-Path $root 'out'
New-Item -ItemType Directory -Force $outDir | Out-Null

$keys = if ($Key -eq 'all') {
    Get-ChildItem $root -Filter '*.md' | Where-Object Name -ne 'README.md' | ForEach-Object BaseName
} else { @($Key) }

foreach ($k in $keys) {
    $src = Join-Path $root "$k.md"
    if (-not (Test-Path $src)) { throw "No source: $src" }
    # Output name: kebab key -> PascalCase file (ai-safety -> AiSafety.docx, study-notes -> StudyNotes.docx)
    $name = ($k -split '-' | ForEach-Object { $_.Substring(0,1).ToUpper() + $_.Substring(1) }) -join ''
    $dst = Join-Path $outDir "$name.docx"

    # Argument array + splatting: readable, and safe to comment line by line
    # (a `# comment` after a backtick continuation is a parse error in PowerShell).
    $args_ = @(
        $src, '-o', $dst,
        '--from', 'markdown+yaml_metadata_block+fenced_divs',   # front matter -> title page; ::: divs -> custom styles
        '--reference-doc', (Join-Path $PSScriptRoot 'reference.docx'),
        '--lua-filter', (Join-Path $PSScriptRoot 'drop-mermaid.lua'),   # Word shows the PNG, not the Mermaid source
        '--resource-path', $root,          # images referenced as assets/x.png resolve
        '--toc', '--toc-depth', '3',
        '--number-sections'                # stable section numbers = citable IDs
    )
    & pandoc @args_
    if ($LASTEXITCODE -ne 0) { throw "pandoc failed for $k" }
    $kb = [math]::Round((Get-Item $dst).Length / 1KB)
    Write-Host "OK  $k -> out/$name.docx ($kb KB)"
}
