# DNS Configuration for evolvingresonantcocreationism.com

## Current Status
Domain is currently pointing to Squarespace servers. We need to redirect it to GitHub Pages.

## Required DNS Changes

### Option 1: Using CNAME (Recommended for root domain)
If your DNS provider supports CNAME flattening or ALIAS records at the root:

```
Type: CNAME (or ALIAS/ANAME)
Name: @ (or leave blank for root)
Value: luminous-dynamics.github.io
TTL: 3600 (or default)
```

### Option 2: Using A Records (If CNAME at root not supported)
Add these four A records:

```
Type: A
Name: @ (or leave blank for root)
Value: 185.199.108.153
TTL: 3600

Type: A
Name: @ (or leave blank for root)
Value: 185.199.109.153
TTL: 3600

Type: A
Name: @ (or leave blank for root)
Value: 185.199.110.153
TTL: 3600

Type: A
Name: @ (or leave blank for root)
Value: 185.199.111.153
TTL: 3600
```

### For www subdomain (Optional but recommended)
```
Type: CNAME
Name: www
Value: luminous-dynamics.github.io
TTL: 3600
```

## Steps by Provider

### If using Squarespace Domains:
1. Log into Squarespace
2. Go to Settings → Domains → evolvingresonantcocreationism.com
3. Click "DNS Settings"
4. Delete existing A records pointing to Squarespace
5. Add the GitHub Pages records above
6. Save changes

### If using GoDaddy:
1. Log into GoDaddy
2. Go to My Products → Domains
3. Click "DNS" next to evolvingresonantcocreationism.com
4. Delete existing A records
5. Add new A records as shown above
6. Save

### If using Namecheap:
1. Log into Namecheap
2. Go to Domain List
3. Click "Manage" next to the domain
4. Go to "Advanced DNS"
5. Remove existing A records
6. Add GitHub Pages A records
7. Save

### If using Cloudflare:
1. Log into Cloudflare
2. Select the domain
3. Go to DNS settings
4. Delete Squarespace A records
5. Add GitHub Pages A records
6. Ensure proxy is OFF (gray cloud) for GitHub Pages to work

## Verification Steps

After making changes:

1. **Wait for propagation** (5 minutes to 48 hours, usually within 1 hour)

2. **Test with dig/nslookup:**
```bash
nslookup evolvingresonantcocreationism.com
# Should return: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
```

3. **Check GitHub Pages status:**
```bash
gh api repos/Luminous-Dynamics/evolving-resonant-cocreationism/pages
# Look for "status": "built" and domain verified
```

4. **Visit the site:**
- http://evolvingresonantcocreationism.com
- Should redirect to HTTPS automatically once verified

## Troubleshooting

### "Domain not verified" in GitHub:
- DNS changes can take up to 48 hours to propagate
- GitHub checks periodically, be patient
- You can force a check by removing and re-adding the CNAME file

### Site shows 404:
- Ensure index.html exists in repository root
- Check that GitHub Pages is enabled for the main branch
- Verify CNAME file contains: evolvingresonantcocreationism.com

### Certificate errors:
- GitHub provides free SSL certificates
- Takes up to 24 hours after domain verification
- Clear browser cache if issues persist

## Quick Check Commands

```bash
# Check current DNS
nslookup evolvingresonantcocreationism.com

# Check if pointing to GitHub
host evolvingresonantcocreationism.com
# Should show: 185.199.108.153, etc.

# Check GitHub Pages status
curl -I https://evolvingresonantcocreationism.com
# Should return HTTP 200 when ready
```

## Support

If you need help finding your DNS settings, check:
- Your domain purchase confirmation email
- Your credit card statements for the registrar
- Try common providers: Squarespace, GoDaddy, Namecheap, Google Domains

---

**Note**: Since the domain currently points to Squarespace, you likely purchased it through Squarespace or transferred it there. Start by checking your Squarespace account.