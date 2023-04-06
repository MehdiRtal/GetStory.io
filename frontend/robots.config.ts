export default [
    {UserAgent: "*"},
    {Disallow: ""},

    // @ts-ignore
    {Sitemap: (req) => `https://${req.headers.host}/sitemap.xml`},
];
