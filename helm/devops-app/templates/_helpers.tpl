{{/*
Nome base do chart
*/}}
{{- define "devops-app.name" -}}
devops-app
{{- end }}

{{/*
Nome completo do release
*/}}
{{- define "devops-app.fullname" -}}
{{ include "devops-app.name" . }}
{{- end }}
