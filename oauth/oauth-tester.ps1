$basePath = (Split-Path $Script:PSCommandPath)
$oauthData = (Get-Content $basePath\oauth-test.json | ConvertFrom-Json)
$auth_domain = $oauthData.auth_domain
$client_id = $oauthData.client_id
$client_secret = $oauthData.client_secret
$oauth_token_url = "$auth_domain/oauth/token"

$Body = @{
    grant_type     = "client_credentials"
    client_id      = $client_id
    client_secret  = $client_secret
    scope          = 'openid'
}

Invoke-RestMethod `
    -Method Post `
    -Body $Body `
    -Uri "${oauth_token_url}" | ConvertTo-Json 
