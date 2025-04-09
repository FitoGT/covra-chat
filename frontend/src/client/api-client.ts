/**
 * Generate a cover letter based on CV and job description
 * @param cv The user's CV
 * @param jobDescription The job description
 * @returns The generated cover letter
 */
export const generateCoverLetter = async (cv: string, jobDescription: string): Promise<string> => {
  try {
    const response = await fetch('http://localhost:8000/generate-cover-letter', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        cv,
        job_description: jobDescription,
      }),
    })

    if (!response.ok) {
      throw new Error('Failed to generate cover letter')
    }

    const data = await response.json()
    return data.cover_letter
  } catch (error) {
    console.error('Error generating cover letter:', error)
    throw error
  }
} 